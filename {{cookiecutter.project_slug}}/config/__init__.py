# flake8: noqa
{% if cookiecutter.use_celery == 'y' -%}
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery_app import app as celery_app
{% endif -%}
{% if cookiecutter.use_drf == 'y' -%}
import os

if os.environ.get("DJANGO_SETTINGS_MODULE") == "config.settings.local":
    import config.schemas # noqa F401
{% endif -%}
{% if cookiecutter.use_celery == 'y' -%}

__all__ = ("celery_app",)
{% endif -%}
