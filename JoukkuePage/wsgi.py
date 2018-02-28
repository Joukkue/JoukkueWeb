"""
WSGI config for JoukkuePage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append("/home/pi/djangoenv/lib/python3.5/site-packages")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JoukkuePage.settings")


from django.core.wsgi import get_wsgi_application


path = '/home/pi/JoukkueWeb'  # use your own username here
if path not in sys.path:
    sys.path.append(path)
os.environ["DJANGO_SETTINGS_MODULE"] = "JoukkuePage.settings"
application = get_wsgi_application()
