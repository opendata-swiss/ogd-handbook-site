#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Open Government Data Switzerland'
SITENAME = u'OGD Handbook'
SITEMAIL = '@'.join(['opendata', 'bar.admin.ch'])
SITEURL = ''

PATH = 'content'
THEME = 'theme'

STATIC_PATHS = [
	'images', 'handbook/images', 'samples',
	'../extra/robots.txt',
	'../extra/favicon.ico',
	'../extra/.htaccess'
]
EXTRA_PATH_METADATA = {
    '../extra/robots.txt': {'path': 'robots.txt'},
    '../extra/favicon.ico': {'path': 'favicon.ico'},
    '../extra/.htaccess': {'path': '.htaccess'}
}

ARTICLE_PATHS = ['handbook','library']
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'
SHOW_ARTICLE_AUTHOR = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = True
DISPLAY_ARTICLE_INFO_ON_INDEX = False
MENUITEMS = []
HIDE_SIDEBAR = True
CC_LICENSE = False

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 8

RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'tipue_search', 'pelican-toc']

JINJA_EXTENSIONS = ['jinja2.ext.i18n']

I18N_SUBSITES = {
	'en': {
		'LOCALE': 'en_US',
		'THEME_STATIC_DIR': 'theme'
		},
	'de': {
		'LOCALE': 'de_CH',
		'THEME_STATIC_DIR': 'theme'
		},
	'fr': {
		'LOCALE': 'fr_CH',
		'THEME_STATIC_DIR': 'theme'
		},
	'it': {
		'LOCALE': 'it_IT',
		'THEME_STATIC_DIR': 'theme'
		}
}

TOC = {
    'TOC_HEADERS' : '^h[1-4]',  # What headers should be included in the generated toc
    'TOC_RUN'     : 'false' # Default value for toc generation
}

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))
