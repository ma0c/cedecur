import os

ALLOWED_HOSTS = [
    # Allowed domains for env
    "142.93.22.249",
]

DATABASE_NAME = os.environ.get("CONFIG_DATABASE_DATABASE", "")
DATABASE_USERNAME = os.environ.get("CONFIG_DATABASE_USERNAME", "")
DATABASE_PASSWORD = os.environ.get("CONFIG_DATABASE_PASSWORD", "")
DATABASE_HOST = os.environ.get("CONFIG_DATABASE_HOST", "")
DATABASE_PORT = os.environ.get("CONFIG_DATABASE_PORT", "")


DATABASES = {
    'default': {
        #
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USERNAME,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT
    }
}
