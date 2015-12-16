# Swiss OGD Handbook #

[opendata.swiss](http://opendata.swiss) will be the official portal for Swiss open government data. All communal, cantonal, and federal authorities and businesses are called on to make data available in open, machine-readable formats, while continuing to ensure privacy and security, using the portal. For further information from the portal team, visit http://ogdch.github.io

The OGD Handbook is being developed to support individuals with responsibilities for data publishing at their government department, as well as the wider user base of the Swiss OGD portal. For these reasons we plan to integrate it within the portal as a centrally accessible, evolving knowledge base.

The structure of the OGD Handbook will be based around visual and contextual representations of the process of data publishing, providing an up-to-date reference for actual and potential data owners. Relevant documentation created as part of the OGD Switzerland project, as well as references from OGD projects around the world to be discoverable within.

We have already interviewed a number of organisations involved in the use and publication of OGD about their organisational readiness from the standpoint of knowledge sharing. The OGD Handbook team continues to gather feedback with a focus on evaluating the structure, quality and usability of learning materials. Such activities help us to be aware of best practices and facilitate knowledge sharing between stakeholders. See Goals and Needs to find out how to get involved.

For more information visit http://www.ogdhandbook.ch

## Overview ##

The web frontend for the Swiss OGD Handbook is documented here. We use the [Pelican](http://getpelican.com) static site generator for Python which you can learn about at [docs.getpelican.com](http://docs.getpelican.com). It can be easily and quickly deployed to any standard web server, as detailed below.

The Handbook content is written using [Markdown](https://bitbucket.org/tutorials/markdowndemo). This is maintained in a [separate repository](https://bitbucket.org/loleg/ch-ogd-handbook) submoduled under `content/handbook`.

The Python-based wiki [realms.io](http://realms.io) was used to create a collaborative environment for editing content, see [deployment instructions](https://github.com/scragg0x/realms-wiki). We are using our own fork with Docker-based [customizations](https://github.com/loleg/realms-wiki/tree/postgres/docker).

We are using the [pelican-bootstrap3](https://bitbucket.org/loleg/ogd-pelican-bootstrap3) theme submoduled under `theme`. For more information see the project's homepage, Pelican's documentation [on themes](http://docs.getpelican.com/en/3.5.0/themes.html), and the [Bootstrap](http://getbootstrap.com/) site.

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

### Translations ###

Using [PyBabel](http://pythonhosted.org/Flask-Babel/#translating-applications) we can keep the theme translations up to date.

```
cd theme/translations
pybabel extract -F babel.cfg -o messages.pot .. --omit-header
pybabel update -i messages.pot -d .
pybabel compile -d . -f
```

To add another language:
```
pybabel init -i messages.pot -d . -l de
```

### Who do I talk to? ###

Send us a note via the contacts on the [public homepage](http://www.ogdhandbook.ch) if you have a question.
