#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR=u'Dustin Stackhouse'
SITENAME=u'Allons-y Blog'
#SITESUBTITLE = u'Adventures learning to code'
#SITEURL = ''

PATH='content'

TIMEZONE='US/Eastern'

DEFAULT_LANG=u'en'

MD_EXTENSIONS=[
    'codehilite',
    'extra',
    'mdx_titlecase',
]
TYPOGRIFY=True

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
FILENAME_METADATA='(?P<slug>.*)'

# Force the same URL structure as WordPress
ARTICLE_URL='{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS=ARTICLE_URL + 'index.html'
ARTICLE_PATHS=['posts']

PAGE_URL='{slug}/'
PAGE_SAVE_AS=PAGE_URL + 'index.html'
PAGE_PATHS=['pages']

###TEMPLATE_PAGES = {}

DIRECT_TEMPLATES=[
    'index', 'tags', 'categories', 'authors', 'archives', 'search']

# Formatting the other urls
CATEGORY_URL="category/{slug}"
CATEGORY_SAVE_AS="category/{slug}/index.html"

TAG_URL="tag/{slug}/"
TAG_SAVE_AS="tag/{slug}/index.html"

# Generate yearly and monthly archive
YEAR_ARCHIVE_SAVE_AS='{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS='{date:%Y}/{date:%m}/index.html'

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS='tags/index.html'
CATEGORIES_SAVE_AS='categories/index.html'
ARCHIVES_SAVE_AS='archives/index.html'

# Deactivate author URLs
AUTHOR_SAVE_AS=False
AUTHORS_SAVE_AS=False

# Deactivate localization
ARTICLE_LANG_SAVE_AS=None
PAGE_LANG_SAVE_AS=None

# Feed generation is usually not desired when developing
FEED_ALL_ATOM=None
CATEGORY_FEED_ATOM=None
TRANSLATION_FEED_ATOM=None
AUTHOR_FEED_ATOM=None
AUTHOR_FEED_RSS=None

USE_FOLDER_AS_CATEGORY=False
DEFAULT_CATEGORY='misc'
DEFAULT_DATE_FORMAT='%b. %d, %Y'
REVERSE_ARCHIVE_ORDER=True
DISPLAY_PAGES_ON_MENU=False
DISPLAY_CATEGORIES_ON_MENU=False
SHOW_ARTICLE_CATEGORY=True
SHOW_DATE_MODIFIED=True

# Pagination
DEFAULT_ORPHANS=2
DEFAULT_PAGINATION=5

# Show most recent posts first
NEWEST_FIRST_ARCHIVES=False

# Define theme being used
THEME='theme/pelican-bootstrap3'
BOOTSTRAP_THEME='superhero'
PYGMENTS_STYLE='solarizeddark'
BANNER='images/banner.png'
BANNER_SUBTITLE=u'Adventures learning to code'
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_TAGS_INLINE=True
TAGS_URL='tags'
#NAVBAR_DEFAULT = True # this for some unknown reason breaks the navabar collapse
#USE_PAGER = True

STATIC_PATHS=[
    'extra',
    'images',
    'extra/CNAME'
]

EXTRA_PATH_METADATA={
    'extra/favicons/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Don't have the plugins included in my repo yet, but place holder
PLUGIN_PATHS=['pelican-plugins']
PLUGINS=[
    'related_posts',
    'tipue_search',
    'neighbors',
    'sitemap',
    'tag_cloud'
]

RELATED_POSTS_MAX=3

SITEMAP={
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

AVATAR='/images/thumbs/firstBlogThumb.jpg'
#SITE_THUMBNAIL_TEXT = 'My poor wife endures a lot ;)'

# Partner links in footer
#LINKS = (('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)
LINKS=None

# Social contact links in footer
SOCIAL=(('Twitter', 'https://twitter.com/dstack4273'),
        ('GitHub', 'https://github.com/dstack4273'),
        ('LinkedIn', 'https://linkedin.com/in/dustinstackhouse'),)

GITHUB_USER='dstack4273'
GITHUB_SKIP_FORK=True
GITHUB_REPO_COUNT=3

# set up some links in the top page menu
MENUITEMS=(
    ('Home', '/'),
    ('Categories', '/categories/'),
    ('Tags', '/tags/'),
    ('About', '/about/'),
)

DISQUS_SITENAME='allonsyblog'
ADDTHIS_PROFILE='ra-57183cbeb445118c'
# The additional hash is too ugly for me to see the value in it - yuck!
ADDTHIS_DATA_TRACK_ADDRESSBAR=False
#GOOGLE_ANALYTICS='placeholder'
