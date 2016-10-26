#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

AUTHOR = 'Inndy'
SITENAME = 'Tech Rain'
SITEURL = ''

SUB_TITLE = '技術需要雨水滋潤才能成長茁壯'
BIO = "It's Inndy speaking."

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('github', 'https://github.com/Inndy'),
    ('twitter', 'https://twitter.com/Inndy_tw'),
)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = [
    'sitemap',
]

SITEMAP = {
    'format': 'xml',
    'exclude': ['tag/', 'category/']
}

STATIC_PATHS = ['assets', 'extra/CNAME']

THEME = '../pelican-hyde/'
PROFILE_PIC = 'https://gravatar.com/avatar/26cdb92aafb2b2e6c8972edebda4bd17?s=360'
