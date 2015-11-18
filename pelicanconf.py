#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'OGD Switzerland Project'
SITENAME = u'Support'
SITEURL = ''

PATH = 'content'
THEME = 'theme'

STATIC_PATHS = [
	'images', 'handbook/images',
	'extra/robots.txt',
	'extra/favicon.ico',
	'extra/.htaccess'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/.htaccess': {'path': '.htaccess'}
}

ARTICLE_PATHS = ['handbook','library']
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = True
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
LINKS = (('Swiss OGD Portal', 'http://opendata.admin.ch/'),
         ('egovernment.ch', 'http://egovernment.ch/ogd'),
		)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/ogdch/ogd-handbook/'),
          ('Twitter', 'https://twitter.com/eGovCH'),
		)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
