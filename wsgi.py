import os
import site

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'src')
PROJECT_LOCAL = os.path.join(PROJECT_ROOT, 'local')
SHARED_ENV = os.path.join(PROJECT_LOCAL, 'shared')
PYTHON_DIR = os.path.join(PROJECT_LOCAL, 'venv', 'lib', 'python2.7')

site.addsitedir(os.path.join(PYTHON_DIR, 'site-packages'))
site.addsitedir(PROJECT_ROOT)
site.addsitedir(PROJECT_PATH)
site.addsitedir(SHARED_ENV)

for path in os.listdir(SHARED_ENV):
    PATH = os.path.join(SHARED_ENV, path)
    if os.path.isdir(PATH):
        site.addsitedir(PATH)

os.environ.setdefault('PYTHON_EGG_CACHE', os.path.join(PROJECT_LOCAL, 'cache', 'egg')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

