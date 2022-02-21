import os

env = os.getenv('DJANGO_ENV')
if env == 'local':
    from .local_settings import *
else:
    from .prod_settings import *
