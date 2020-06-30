#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'tai271828'
SITENAME = 'tai 的網誌'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
            ('My Blog (en)', 'https://tai271828.github.io'),
            ('SOLVCON', 'https://solvcon.net'),
            ('PyCon TW (repository)', 'https://github.com/pycontw'),
        )

# Social widget
SOCIAL = (
            ('LinkedIn', 'https://linkedin.com/in/tai271828'),
            ('Twitter', 'https://twitter.com/tai271828'),
            ('Github', 'https://github.com/tai271828'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme
THEME = 'themes/backdrop'
# github issue #386
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
BACKDROP_IMAGE = 'theme/sodtube.png'
PROFILE_IMAGE = 'theme/tai.png'
FAVICON = 'theme/tai.png'
SITE_DESCRIPTION = 'Python, HPC, Ubuntu, Science, and Physics. Mountaineer, climber, pianist, and cellist.'
EMAIL = 'tai271828@gmail.com'
