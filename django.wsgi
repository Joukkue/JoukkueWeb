import os
import sys

path='/home/pi/JoukkueWeb/django.wsgi'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'joukkuepage.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
