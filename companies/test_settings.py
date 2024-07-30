from .settings import *             # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ':memory:'
    }
}
