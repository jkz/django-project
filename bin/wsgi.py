import os
import sys

sys.stdout = sys.stderr

os.environ.setdefault('PYTHON_EGG_CACHE', os.path.join(LOCAL, 'cache', 'egg')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

