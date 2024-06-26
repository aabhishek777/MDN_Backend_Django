
from pathlib import Path
import environ

env= environ.Env()

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

print(ROOT_DIR)


APP_DIR= ROOT_DIR/"core_apps"

DEBUG= env.bool("DJANGOD_DEBUG",False)

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites"
]

THIRD_PARTY_APPS=[
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    "drf_yasg",
    "corsheaders"
]

LOCAL_APPS= [
    "core_apps.profiles",
    "core_apps.common",
    "core_apps.users",
]

INSTALLED_APPS= DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "author_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "author_api.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": "mydb",
#     }
# }

DATABASES= {
    "default":env.db("DATABASE_URL")
}




PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

SITE_ID=1

ADMIN_URL="supersecret/"

STATIC_URL = "staticFiles/"

STATIC_ROOT= str(ROOT_DIR/"staticFiles")

MEDIA_URL = "mediaFiles/"

MEDIA_ROOT= str(ROOT_DIR/"medialFiles")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORES_URLS_REGEX= r"^api/.*$"

LOGGING={
    "version":1,
    "disable_existing_logger":False,
    "formatters": {
         "verbose":{
            "format":"%(levelname)s %(name)-12s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(messages)s"
        }
    },
     "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    }
}