#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bohumír Zámečník'
SITENAME = 'Visual Music Theory'
SITEURL = ''
SITE_DESCRIPTION='Music theory, processing, visualization, analysis'

PATH = 'content'

THEME='/Users/bzamecnik/python/pelican/pelican-themes/pelican-elegant'

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
SOCIAL = (
    ('Twitter', 'https://twitter.com/bzamecnik'),
    ('GitHub', 'https://github.com/bzamecnik'),
    ('LinkedIn', 'https://cz.linkedin.com/in/bohumirzamecnik'),
)

DEFAULT_PAGINATION = 10

LOCALE = ('en_US')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_EXCLUDES=['skype-lessons']

STATIC_PATHS = ['images']

# Elegant Labels
SOCIAL_PROFILE_LABEL = 'Stay in Touch'
# RELATED_POSTS_LABEL = 'Keep Reading'
# SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = 'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

