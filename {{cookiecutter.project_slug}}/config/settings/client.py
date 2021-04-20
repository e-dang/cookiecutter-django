"""
Settings for test client in functional tests
"""

from .base import env
from .test import *  # noqa

APP_HOST_NAME = env("APP_HOST_NAME", default="django")
SELENIUM_HUB_HOST_NAME = env("SELENIUM_HUB_HOST_NAME", default="hub")
BROWSER = env("BROWSER", default="firefox")
