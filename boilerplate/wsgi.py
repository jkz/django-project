import os
import sys
sys.stdout = sys.stderr

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.split(PROJECT_PATH)[1]
PROJECT_ROOT = os.path.join(PROJECT_PATH, '..')
PROJECT_LOCAL = os.path.join(PROJECT_ROOT, 'local')

# Add the virtual Python environment site-packages directory to the path
import site

PYTHON_DIR = os.path.join(PROJECT_LOCAL, 'venv', 'lib', 'python2.7')
site.addsitedir(os.path.join(PYTHON_DIR, 'site-packages'))

SHARED_ENV = os.path.join(PROJECT_LOCAL, 'shared_env')
for path in os.listdir(SHARED_ENV):
    PATH = os.path.join(SHARED_ENV, path)
    if os.path.isdir(PATH):
        site.addsitedir(PATH)

import os
# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
os.environ['PYTHON_EGG_CACHE'] = os.path.join(PROJECT_LOCAL, 'cache', 'egg')

#If your project is not on your PYTHONPATH by default you can add the following
sys.path.append(PROJECT_ROOT)
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import djcelery
djcelery.setup_loader()
