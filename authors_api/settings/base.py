import os
from pathlib import Path
from datetime import timedelta
import environ

# Initialize environment variables
env = environ.Env()

# Define the root directory
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from the .env files
environ.Env.read_env(os.path.join(ROOT_DIR, '.envs', '.local', '.django'))
environ.Env.read_env(os.path.join(ROOT_DIR, '.envs', '.local', '.postgres'))

# Directory for core apps
APP_DIR = ROOT_DIR / "core_apps"

# Debug setting
DEBUG = env.bool("DJANGO_DEBUG", False)

# Installed apps
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    "drf_yasg",
    "corsheaders",
    "djcelery_email",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "rest_framework.authtoken"
]

LOCAL_APPS = [
    "core_apps.profiles",
    "core_apps.common",
    "core_apps.users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

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

ROOT_URLCONF = "authors_api.urls"

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

WSGI_APPLICATION = "authors_api.wsgi.application"

# Database configuration
DATABASES = {
    "default": env.db("DATABASE_URL")
}

# Password hashers
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# Password validation
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

# Localization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Calcutta"
USE_I18N = True
USE_TZ = True

# Site ID
SITE_ID = 1

# Admin URL
ADMIN_URL = "supersecret/"

# Static files settings
STATIC_URL = "staticFiles/"
STATIC_ROOT = str(ROOT_DIR / "staticFiles")

# Media files settings
MEDIA_URL = "mediaFiles/"
MEDIA_ROOT = str(ROOT_DIR / "mediaFiles")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS URLs regex
CORES_URLS_REGEX = r"^api/.*$"

# Custom user model
AUTH_USER_MODEL = "users.User"

# celery configuration to perform asynchronous tasks like mailing etc
CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_BROKER_BACKEND = CELERY_BROKER_URL
# we can pass the content type here 
CELERY_ACCEPT_CONTENT= ['json',]
CELERY_TASK_SERIALIZER= "json"
CELERY_RESULT_SERIALIZER= "json"
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CELERY_TASK_SEND_SENT_EVENT = True

if USE_TZ:
    CELERY_TIMEZONE= TIME_ZONE


REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": [
                "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        ],

        "DEFAULT_PERMISSION_CLASSES": [
                "rest_framework.permissions.IsAuthenticated",
        ],
        "DEFAULT_FILTER_BACKENDS": [
                "django_filters.rest_framework.DjangoFilterBackend",
                ]
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES":("Bearer",),
    "ACCESS_TOKEN_LIFETIME":timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME":timedelta(days=5),
    "ROTATE_REFRESH_TOKEN":True,
    "SIGNING_KEY":env.get_value("SIGNING_KEY")
    
}

# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    }
}
