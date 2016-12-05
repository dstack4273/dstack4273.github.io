#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL='http://allonsyblog.com'
RELATIVE_URLS=False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY=True

# Following items are often useful when publishing

DISQUS_SITENAME='allonsyblog'
ADDTHIS_PROFILE='ra-57183cbeb445118c'
# The additional hash is too ugly for me to see the value in it - yuck!
ADDTHIS_DATA_TRACK_ADDRESSBAR=False
#GOOGLE_ANALYTICS = ""
