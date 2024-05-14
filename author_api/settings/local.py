
from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",default="django-insecure-p23p((f4%5of-h$ke1d77_9&wefy7x1il09&q1tyuew6+18gim",
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CSRF_TRUSTED_ORIGINS=["http://localhost:8080"]


