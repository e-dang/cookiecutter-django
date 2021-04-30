"""
Settings for test client in functional tests
"""

from .base import env
from .test import *  # noqa

TARGET_ENV = env("TARGET_ENV", default="local")
APP_HOST_NAME = env("APP_HOST_NAME", default="django")
APP_VIRTUAL_HOST_NAME = env("APP_VIRTUAL_HOST_NAME", default="example.local")
SELENIUM_HUB_HOST_NAME = env("SELENIUM_HUB_HOST_NAME", default="hub")
MAILHOG_HOST_NAME = env("MAILHOG_HOST_NAME", default="mailhog")
MAILHOG_PORT = env("MAILHOG_PORT", default="8025")
BROWSER = env("BROWSER", default="firefox")
