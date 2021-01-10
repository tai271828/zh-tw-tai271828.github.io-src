#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'tai271828'
SITENAME = 'tai 的網誌'
SITEURL = 'tai271828.netlify.app'
USER_LOGO_URL = 'images/LTconsulting-v1-150x150.png'
INDEX_TITLE = "tai's blog"
INDEX_DESC = 'Python, HPC, Ubuntu, Science, and Physics. Mountaineer, climber, pianist, and cellist.'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = "%b %d, %Y"

THEME = "themes/voce"

PLUGIN_PATHS = ["plugins", os.path.join(THEME, "plugins")]
PLUGINS = ["summary"]

LOAD_CONTENT_CACHE = False
SLUGIFY_SOURCE = 'basename'


EXTRA_PATH_METADATA = {
    'files/favicon.ico': {'path': 'favicon.ico'},
    'files/robots.txt': {'path': 'robots.txt'},
}

#Theme specific
GOOGLE_ANALYTICS_ID = ""
GOOGLE_ANALYTICS_PROP = ""
# GTM ID is optional
# If you don't use GTM, it is ok to leave it as an empty string.
GTM_ID = "GTM-K5KVL4G"
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
# use less max length for zh blog because for none-latin or cjk, one sentance
# will be treated as "a word" so the summary will be too long
# refer to the discussion thread of pelican issue #1180
# https://github.com/getpelican/pelican/issues/1180
SUMMARY_MAX_LENGTH = 2

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
