# -*- coding: utf-8 -*-
import sys

sys.path.append('../../../')

from shared.conf import *

# General information about the project.
project = u'Installing, Configuring, and Running the Open edX Platform'
set_audience(OPENEDX, DEVELOPERS)

# remove directory when content is first added to it, and add to index
exclude_patterns = ['links.rst', 'configuration/configure_milestone_app.rst']
