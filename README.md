# OGD Handbook Site #

This repository contains web application source code for the OGD Handbook. For more information, visit http://handbook.opendata.swiss

## Overview ##

The web frontend for the OGD Handbook is documented here. We use the [Pelican](http://getpelican.com) static site generator for Python which you can learn about at [docs.getpelican.com](http://docs.getpelican.com). It can be easily and quickly deployed to any standard web server, as detailed below.

The Handbook content is written using [Markdown](https://bitbucket.org/tutorials/markdowndemo). This is maintained in a [separate repository](https://bitbucket.org/loleg/ch-ogd-handbook) submoduled under `content/handbook`.

The Python-based wiki [realms.io](http://realms.io) was used to create a collaborative environment for editing content, see [deployment instructions](https://github.com/scragg0x/realms-wiki). We are using our own fork with Docker-based [customizations](https://github.com/loleg/realms-wiki/tree/postgres/docker).

We are using the [Pelican Bootstrap 3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) theme. For more information see the project's homepage, Pelican's documentation [on themes](http://docs.getpelican.com/en/3.5.0/themes.html), and the [Bootstrap](http://getbootstrap.com/) site.

The following documentation deals with installation of the web frontend.

### Setup ###

1) Clone this repository, then go into the folder and update submodules:

```
git submodule update --init --recursive
```

2) Create and initialise the virtual environment:

```
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

3) Run the development server

```
./develop_server.sh start 8080
```

You can now access the website on http://localhost:8080

### Configuration ###

Please see [Pelican documentation](http://docs.getpelican.com/en/latest/settings.html) for information on configuring for deployment.

### Contribution guidelines ###

We accept pull requests to this repository for changes to the web site only.

### Deployment notes ###

1) Set up LFTP for syncing (one time)

```
sudo apt-get install lftp
mkdir ~/.lftp
echo "set ssl:verify-certificate no" > ~/.lftp/rc
```

2) Run deployment script

Re-run the publish command to ensure that assets are correctly formatted. Then upload to the server. You will be asked for an FTP password.

```
make publish
make ftp_upload
```

After deployment, ensure links are working in the Topics page, else you may need to re-run your publishing steps.

#### Document export ####

To generate LibreOffice and Word versions of the Handbook pages, we use pandoc. The latest version (1.15+ is required) can be installed by downloading a binary [from this page](https://github.com/jgm/pandoc/releases/).

The files will be generated in the `/export` folder of output using

```
make publish
make doc_export
```

### Translations ###

Using [Babel](http://babel.pocoo.org/) for [Flask](http://pythonhosted.org/Flask-Babel/#translating-applications), we can keep the theme translations up to date. Use the script in the root folder:

```
./update_translations.sh
```

To add another language:
```
cd theme/translations
pybabel init -i messages.pot -d . -l de
```

### Who do I talk to? ###

Send us a note via the contacts on [the homepage](http://handbook.opendata.swiss) if you have a question.
