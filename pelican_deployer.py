"""
Deployment script

Simple web server that listens for Github webhooks to implement push-to-deploy
with (multiple) Pelican static sites. All settings are loaded from a json file.

Based on gist by Mark Steve Samson https://gist.github.com/marksteve/8243318

Example `deployerconf.json`:
```
{
  "repos": {
    "mysite": {
      "root": "/path/to/repo",
      "secret": "mysecret",
      "remote": "origin",
      "ftp": {
        "user": "myusername",
        "host": "ftp.host.url",
        "pwd": "mysecretpasswd",
        "dir": "/target/path",
      }
    }
  }
}
```

Run it

```
$ python ./pelican_deployer.py deployerconf.json
```
or (with deployerconf.json as default)
```
$ gunicorn pelican_deployer.py -b localhost:5000
```

Add http://<deployer_host>/{mysite}/{mysecret} as a webhook url and you're done
"""
import logging
import os
import subprocess
import sys

from flask import Flask, json, jsonify, request

app = Flask(__name__)

def sh(cmd, **kwargs):
    cmd = cmd.format(**kwargs)
    output = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True,
    )
    app.logger.info('\n' + cmd)
    app.logger.info('\n'.join([' > ' + l for l in output.split('\n')]))
    return output

@app.route('/<repo_id>/<repo_secret>', methods=['POST'])
def deploy(repo_id, repo_secret):
    payload = json.loads(request.form['payload'])
    repo = app.config['repos'][repo_id]
    if repo_secret != repo['secret']:
        return jsonify(dict(ok=False))
    os.chdir(repo['root'])
    sh(
        'git pull --ff-only {remote} {branch}',
        remote=repo.get('remote', 'origin'),
        branch=repo.get('branch', 'master')
    )
    sh(
        'git submodule foreach git pull --ff-only {remote} {branch}',
        remote=repo.get('remote', 'origin'),
        branch=repo.get('branch', 'master')
    )
    publish_output = sh(
        'make publish'
    )
    if 'Error' in publish_output:
        return jsonify(dict(ok=False, error=publish_output))
    sh (
        'lftp -u {ftp_user},{ftp_pwd} {ftp_host} -e "mirror --no-perms -R {root_dir}/output {ftp_dir}; quit"',
        ftp_user=repo['ftp'].get('user'),
        ftp_pwd=repo['ftp'].get('pwd'),
        ftp_host=repo['ftp'].get('host'),
        ftp_dir=repo['ftp'].get('dir'),
        root_dir=repo['root']
    )
    # sh(
    #   'pelican -d -o {output} content',
    #   output=repo['output'].format(branch=branch, **payload),
    # )
    return jsonify(dict(ok=True))


if __name__ == '__main__':
  if len(sys.argv)<1:
    fname = sys.argv[1]
  else:
    fname = 'deployerconf.json'
  with open(fname) as f:
    app.config.update(**json.load(f))
  app.logger.addHandler(logging.StreamHandler())
  app.logger.setLevel(logging.INFO)
  app.run()
