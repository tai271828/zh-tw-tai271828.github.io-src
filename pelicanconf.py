#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'tai271828'
SITENAME = 'tai 的網誌'
SITEURL = 'tai271828.netlify.app'
USER_LOGO_URL = 'http://i.imgur.com/zzCRZUH.jpg'
INDEX_TITLE = 'Site Title'
INDEX_DESC = 'Description of Site'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = "%b %d, %Y"

THEME = "themes/voce"

PLUGIN_PATHS = ["plugins", os.path.join(THEME, "plugins")]

LOAD_CONTENT_CACHE = False
SLUGIFY_SOURCE = 'basename'


EXTRA_PATH_METADATA = {
    'files/favicon.ico': {'path': 'favicon.ico'},
    'files/robots.txt': {'path': 'robots.txt'},
}

#Theme specific
GOOGLE_ANALYTICS_ID = "UA-123456-7"
GOOGLE_ANALYTICS_PROP = "siteurl.com"
TAGLINE = "Site Tagline"
MANGLE_EMAILS = False
GLOBAL_KEYWORDS = ("keywords",)


SOCIAL = (
    ('LinkedIn', 'https://linkedin.com/in/tai271828'),
    ('Twitter', 'https://twitter.com/tai271828'),
    ("GitHub", "https://github.com/tai271828"),
    #("Feed", "https://siteurl.com/feeds/all.atom.xml"),
)

LINKS = (
    ("Index", "/index.html"),
    #("About me", "/pages/about-me.html"),
)

DEFAULT_PAGINATION = 8

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 50

ARCHIVES_URL = "archives.html"
ARCHIVES_SAVE_AS = 'archives.html'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAGS_URL = 'tag/{slug}.html'

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

DEFAULT_METADATA = {
    'status': 'draft',
}
