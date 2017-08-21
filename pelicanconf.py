# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Flavio Percoco'
SITENAME = u'De 5 a 10 minutos'
SITEURL = os.environ.get('SITEURL', 'https://vlog.flaper87.com')
#GOOGLE_ANALYTICS = 'UA-54541847-1'

PATH = 'content'
THEME = './theme/flaper87'

STATIC_PATHS = ['img']
EXTRA_PATH_METADATA = {}

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'es'

MARKDOWN = {
    'output_format': 'html5',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/flaper87'),
          ('github', 'https://github.com/test'),)
TWITTER_USERNAME = "flaper87"

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

DEFAULT_PAGINATION = 5
TYPOGRIFY = False

PLUGIN_PATHS = [os.path.join(os.path.dirname(__file__), 'pelican-plugins')]
PLUGINS = [
    'liquid_tags.youtube',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
