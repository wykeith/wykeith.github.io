#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wykeith Ng'
SITENAME = 'Data Thoughts'
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'Urbanist - Geek - Maker'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
#SITELOGO = '//avatars2.githubusercontent.com/u/13540132?v=3&s=460'
SITELOGO = '/images/avatar.jpeg'

THEME = './themes/Flex'
ROBOTS = 'index, follow'
PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Email', 'mailto:wykeith@gmail.com'),
         ('Resume', '/pdfs/resume-may2019.pdf'),
         ('Thesis', 'https://sites.google.com/site/wykeith/Thesis'),)

# Social widget
SOCIAL = (('linkedin', 'https://sg.linkedin.com/in/wykeith/en'),
          ('github', 'https://github.com/wykeith'),
          ('google', 'https://plus.google.com/+WykeithNG'),
          #('twitter', 'https://twitter.com/wykeithng'),
          ('rss', '/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
