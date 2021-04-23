#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime
AUTHOR = 'Boni'
SITENAME = "Boni Oloff"
SITEURL = 'https://bonioloff.github.io'
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'EN'
SITESUBTITLE = "Learn and Work"
SITETITLE = "Boni Oloff"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 5
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = '../Flex'
STATIC_PATHS = ['img', 'static']
FAVICON = SITEURL + "/img/profile.jpg"
SITELOGO = SITEURL + "/img/profile.jpg"
CUSTOM_CSS = 'static/custom.css'
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['neighbors', 'tipue_search', 'post_stats', 'representative_image']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']
LINKS = (
    ("Projects", "#"),
)
SOCIAL = (
    ("github", "https://github.com/bonioloff"),
    ("linkedin", "https://www.linkedin.com/in/bonioloff"),
    ("kaggle", "https://www.kaggle.com/bonioloff"),
    ("gitlab", "https://gitlab.com/bonioloff")
)
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = False
THEME_COLOR = 'light'
PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'
COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = "Boni Oloff"
ROBOTS = "index, follow"

# CC_LICENSE = {
#     "name": "Creative Commons Attribution-ShareAlike",
#     "version": "4.0",
#     "slug": "by-sa"
# }
