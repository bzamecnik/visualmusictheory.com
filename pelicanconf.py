#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bohumír Zámečník'
SITENAME = 'Visual Music Theory'
SITEURL = '' # SITEURL = 'http://visualmusictheory.com'

PATH = 'content'

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
    ('Neural Thoughts', 'http://neural.cz/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/bzamecnik'),)

DEFAULT_PAGINATION = 10

LOCALE = ('en_US')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_EXCLUDES=['skype-lessons']
