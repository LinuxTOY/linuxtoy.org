#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'toy'
SITENAME = u'LinuxTOY'
SITEURL = 'https://linuxtoy.org'

PATH = 'content'
STATIC_PATHS = ['images', 'files']
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
DEFAULT_CATEGORY = 'News'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

SUMMARY_MAX_LENGTH = 30
DEFAULT_PAGINATION = 10

AUTHOR_ALIAS = {
        'lovenemesis': '黑日白月',
        'wsgzao': '王奥OX',
        'yutangbaihe': '玉堂白鹤',
        'jianlee': '好风',
        }

#PAGE_ICONS = ['folder', 'book', 'support', 'mail', 'heart', 'exclamationCircle']
#RSS_ICONS = ['rss']
DISPLAY_PAGES_ON_MENU = True
MENUITEMS_AFTER = (('Comments', '/pages/comments.html'), ('Random', '/random.html'), ('RSS', '/feeds/all.atom.xml'),)

GITHUB_SOURCE = 'https://github.com/LinuxTOY/linuxtoy.org/blob/master/content'

DISQUS_SITENAME = 'linuxtoy'
GOOGLE_ANALYTICS = 'UA-349050-2'
SWIFTYPE = 'zWjtxRdA6ciZ7LBm4R4K'
TWITTER_NAME = '@linuxtoy'

ARTICLE_URL = 'archives/{slug}.html'
ARTICLE_SAVE_AS = 'archives/{slug}.html'

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'

FEED_MAX_ITEMS = 10
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

THEME = 'themes/itoy'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-page-order', 'summary', 'neighbors', 'related_posts', 'random_article']

CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'

RELATED_POSTS_MAX = 5
RANDOM = 'random.html'
