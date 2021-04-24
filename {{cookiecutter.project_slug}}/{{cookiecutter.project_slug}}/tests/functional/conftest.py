import pytest
from django.conf import settings
from selenium import webdriver


@pytest.fixture
def selenium_hub_url():
    return f"http://{settings.SELENIUM_HUB_HOST_NAME}:4444/wd/hub"


@pytest.fixture
def server_url():
    return f"http://{settings.APP_HOST_NAME}"


@pytest.fixture
def web_driver(selenium_hub_url):
    caps = {"browserName": settings.BROWSER}
    driver = webdriver.Remote(command_executor=selenium_hub_url, desired_capabilities=caps)

    yield driver

    driver.quit()
