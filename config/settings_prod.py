import os

ALLOWED_HOSTS = [
    # Allowed domains for env
    "config.contraslash.com",
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


AWS_ACCESS_KEY_ID = os.environ.get("CONFIG_AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("CONFIG_AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("CONFIG_AWS_STORAGE_BUCKET_NAME", "")
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://{}/'.format(AWS_S3_CUSTOM_DOMAIN)
