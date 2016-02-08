#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dustin Stackhouse'
SITENAME = u'Allons-y Blog'
SITESUBTITLE = u'| Adventures learning to code'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Not sure I want to copy this from Kevin's yet, the pelican docs make it sound
#like you get less markdown capability by defining only a few.
# MD_EXTENSIONS = [
#     'codehilite',
#     'extra',
#     'mdx_video',
#     'mdx_titlecase',
# ]
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
FILENAME_METADATA = '(?P<slug>.*)'

# Force the same URL structure as WordPress
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_PATHS = ['posts']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['pages']

DIRECT_TEMPLATES = [
    'index', 'tags', 'categories', 'authors', 'archives', 'search']

# Formatting the other urls
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly and monthly archive
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False

# Pagination
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 5

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

# Define theme being used
THEME = "pelican-themes/plumage"

STATIC_PATHS = [
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicons/favicon.ico': {'path': 'favicon.ico'},
}

#Don't have the plugins included in my repo yet, but place holder
# PLUGIN_PATHS = ['plugins-core']
# PLUGINS = [
#     # Core plugins
#     'related_posts',
#     # 'thumbnailer',
#     'tipue_search',
#     'neighbors',
#     'sitemap',
# ]

#SITE_THUMBNAIL =
#SITE_THUMBNAIL_TEXT =

# Partner links in footer
LINKS = (('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)


# Social contact links in footer
SOCIAL = (('Twitter', 'https://twitter.com/dstack4273'),
          ('GitHub', 'https://github.com/dstack4273'),
          ('LinkedIn', 'https://linkedin.com/in/dustinstackhouse'),)


# set up some links in the top page menu
MENUITEMS = (
    ('Home', '/'),
    ('Topics', '/categories/'),
    ('Tags', '/tags/'),
    ('About', '/about/'),
)

#Haven't made this yet
#DISQUS_SITENAME =
