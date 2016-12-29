"""Development settings and globals."""

from .base import *

########## DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ########## END EMAIL CONFIGURATION


# ########## DATABASE CONFIGURATION
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }
# ########## END DATABASE CONFIGURATION


# ########## CACHE CONFIGURATION
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    # }
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
# ########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
# ########## END TOOLBAR CONFIGURATION
