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

PLUGIN_PATHS = ['/Users/bzamecnik/python/pelican/pelican-plugins']

PLUGINS = [
    'sitemap',
    # 'extract_toc',
    'tipue_search',
    # 'pelican_youtube'
]
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Elegant Labels
SOCIAL_PROFILE_LABEL = 'Stay in Touch'
# RELATED_POSTS_LABEL = 'Keep Reading'
# SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = 'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = 'Never miss an article'
EMAIL_FIELD_PLACEHOLDER = 'Enter your email'
SUBSCRIBE_BUTTON_TITLE = 'Send me free updates'
# group[981][4]=1 = "Music Theory"
MAILCHIMP_FORM_ACTION = 'http://bohumirzamecnik.us12.list-manage1.com/subscribe?u=132db635fd4dc81131d9491db&id=f15d396091&group[981][4]=1'
