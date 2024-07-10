
from .celery import app as celery_app

# exporting tuple for all apps here

__all__ = ("celery_app",)