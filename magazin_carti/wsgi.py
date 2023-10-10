"""
WSGI config for magazin_carti project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import django_settings_file


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magazin_carti.settings')
os.environ.setdefault('DJANGO_SETTINGS_FILE', '/path/to/default.py')
application = get_wsgi_application()
