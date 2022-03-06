import os

env = os.getenv('DJANGO_ENV')
if env == 'compose':
    from .compose_settings import *
elif env == 'staging':
    from .staging_settings import *
elif env == 'prod':
    from .prod_settings import *
else:
    from .local_settings import *
