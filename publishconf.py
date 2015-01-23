#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.visualmusictheory.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "visualmusictheory"
GOOGLE_ANALYTICS = "UA-44857522-3"
#GITHUB_URL='https://github.com/bzamecnik/visualmusictheory.com'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico', 'skype-lessons']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
ARTICLE_EXCLUDES=['skype-lessons']
