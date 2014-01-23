#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Will Ouyang'
SITENAME = u'EVA'
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

LOCALE = ('usa',  # On Windows
    'en_US'     # On Unix/Linux
)
DATE_FORMATS = {
    'en': '%a %d %B %Y',
}
DEFAULT_DATE = (2013, 6, 27, 10, 1, 1)
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'bootstrapTheme4eva'

DISQUS_SITENAME = 'evaimg'
#TWITTER_USERNAME = 'oeway'
#GITHUB_URL = 'https://github.com/evaimg/EVA'
GOOGLE_ANALYTICS='UA-47365192-1'

NDE_CATEGORIES = (
            
            ('Bioimaging','pages/bioimaging.html'),
            ('-','-'),
            ('Ultrasonic','pages/ultrasonic.html'),
            ('Radiography', 'pages/radiography.html'),
            ('Eddy-current', 'pages/eddycurrent.html'),
            ('-','-'),
            
            
            )
MENUITEMS =(('Home',''),
            ('Blog','blog.html'),
            ('Wiki','http://wiki.evaimg.org'),
            #('Categories_dropdown', NDE_CATEGORIES ),
            ('Downloads','pages/downloads.html'),
            ('About','pages/about.html'),
            )

CAROUSELITEMS = (
            {
            'image':'images/slide-01.png',  
            'headline':'Imaging and Evaluation',
            'subtitle':'An Open-souce Platform',
            'buttonLink':'pages/about.html',
            'buttonCaption':'Learn More',
            },
            
)
# static paths will be copied without parsing their contents
STATIC_PATHS = [
                'extra/robots.txt',
                'CNAME',
                'images'
                ]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives','blog','editor')
PLUGINS_SAVE_AS = 'blog.html'

USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'


# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
         
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

