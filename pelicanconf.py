#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Neill Cox'
SITENAME = 'Sceptical Believer'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['blog']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('OpenStack', 'https://www.openstack.org/'),
         ('Python.org', 'http://python.org/'),
         )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/neillc'),
          ('Twitter', 'https://twitter.com/neillcox'),
          ('LinkedIn', 'https://www.linkedin.com/in/neill-cox-467650a/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
