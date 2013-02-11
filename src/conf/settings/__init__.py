"""
from path import path
#import django

# DJANGO_ROOT = path(django.__file__)
PROJECT_PATH = path(__file__).parent.parent
PROJECT_NAME = PROJECT_ROOT.name
PROJECT_LOCAL = PROJECT_ROOT.parent / 'local'

_env_file = PROJECT_LOCAL / 'ENVIRONMENT'
if _env_file.isfile():
    with open(env_file) as f:
        env = f.read()
else:
    env = 'dev'
#try:
#    module = __import__(env)
#except (ImportError, NameError):
#    module = __import__('test')

exec('from %s import *' % env)
"""

try:
    from .local import *
except ImportError:
    from .default import *
