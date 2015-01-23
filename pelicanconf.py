#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bohumír Zámečník'
SITENAME = 'Visual Music Theory'
SITEURL = ''
SITE_DESCRIPTION='Music theory, processing, visualization, analysis'

PATH = 'content'

THEME='/Users/bzamecnik/python/pelican/pelican-themes/bza_aboutwilson'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Bohumír Zámečník', 'http://bohumirzamecnik.cz/'),
    ('Neural Thoughts - machine learning', 'http://neural.cz/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/bzamecnik'),)

DEFAULT_PAGINATION = 10

LOCALE = ('en_US')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_EXCLUDES=['skype-lessons']

#STATIC_PATHS = ['images', 'fooimages']

STATIC_PATHS = ['extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}