import site
import path

SOURCE = path.path(__file__).parent.parent.parent
LOCAL = SOURCE.parent / 'local'

site.addsitedir(SOURCE)

PACKAGES = (
    'apps',
    'libs',
)

for package in PACKAGES:
    if path.path(SOURCE / package).isdir():
        site.addsitedir(SOURCE / package)

DEBUG = False
VERBOSE = False
TEMPLATE_DEBUG = DEBUG

USE_I18N = False
USE_L10N = True
USE_SESSION = True
USE_CACHE = False
USE_SOUTH = False
USE_CELERY = False


ADMINS = (
     ('Jesse Zwaan', 'j.k.zwaan@gmail.com'),
)

MANAGERS = ADMINS

from fnmatch import fnmatch
class glob_list(list):
    """Allows wildcards in ip addresses"""
    def __contains__(self, key):
        for elt in self:
            if fnmatch(key, elt): return True
        return False

INTERNAL_IPS = glob_list([
    '127.0.0.1',
])

LANGUAGE_CODE = 'en-us'

STATIC_URL = '/static/'
STATIC_ROOT = LOCAL / 'data' / 'static'

STATICFILES_DIRS = (
    SOURCE / 'assets',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = LOCAL / 'data' / 'media'

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'entry.application'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

TEMPLATE_DIRS = (
    SOURCE / 'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.staticfiles',

    'utils',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.ModelBackend',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    "conf.context_processors.static",
)

common = 'django.middleware.common.CommonMiddleware'

if USE_CACHE:
    update = 'django.middleware.cache.UpdateCacheMiddleware'
    fetch = 'django.middleware.cache.FetchFromCacheMiddleware'
    try:
        index = MIDDLEWARE_CLASSES.index(common)
    except ValueError:
        MIDDLEWARE_CLASSES = (update, fetch) + MIDDLEWARE_CLASSES
    else:
        MIDDLEWARE_CLASSES = (update, common, fetch) + MIDDLEWARE_CLASSES[:index] + MIDDLEWARE_CLASSES[index + 1:]

if USE_SOUTH:
    INSTALLED_APPS += (
        'south',
    )


if USE_SESSION:
    SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
    INSTALLED_APPS += (
        'django.contrib.sessions',
    )

    session = 'django.contrib.sessions.middleware.SessionMiddleware'
    try:
        index = MIDDLEWARE_CLASSES.index(common)
    except ValueError:
        MIDDLEWARE_CLASSES = (session,) + MIDDLEWARE_CLASSES
    else:
        MIDDLEWARE_CLASSES = (common, session) + MIDDLEWARE_CLASSES[:index] + MIDDLEWARE_CLASSES[index + 1:]


if USE_CELERY:
    INSTALLED_APPS += (
        'djcelery',
        'kombu.transport.django',
    )

    CELERY_IMPORTS = [
        'myapp.tasks',
    ]

    import djcelery
    djcelery.setup_loader()
