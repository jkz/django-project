import os
import sys
sys.stdout = sys.stderr

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.join(PROJECT_PATH, '..')
PROJECT_LOCAL = os.path.join(PROJECT_ROOT, 'local')

# Add the virtual Python environment site-packages directory to the path
import site

PYTHON_DIR = os.path.join(PROJECT_LOCAL, 'venv', 'lib', 'python2.7')
site.addsitedir(os.path.join(PYTHON_DIR, 'site-packages'))

# Add all the shared environment and all contined packages to the path
SHARED_ENV = os.path.join(PROJECT_LOCAL, 'shared')
site.addsitedir(SHARED_ENV)
for path in os.listdir(SHARED_ENV):
    PATH = os.path.join(SHARED_ENV, path)
    if os.path.isdir(PATH):
        site.addsitedir(PATH)

# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
os.environ['PYTHON_EGG_CACHE'] = os.path.join(PROJECT_LOCAL, 'cache', 'egg')

site.addsitedir(PROJECT_ROOT)
site.addsitedir(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import djcelery
djcelery.setup_loader()
