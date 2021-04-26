import os

import pytest
from django.conf import settings
from selenium import webdriver


@pytest.fixture(autouse=True)
def reset_database():
    ret = os.system(f"docker exec -i {settings.APP_HOST_NAME} /bin/bash < /flush")
    if ret != 0:
        pytest.fail(msg=f"Failed to flush the database. Command exited with a return code of {ret}.")


@pytest.fixture
def ssl_ca_cert():
    return f"{settings.ROOT_DIR}/certs/rootCA.pem"


@pytest.fixture
def selenium_hub_url():
    return f"http://{settings.SELENIUM_HUB_HOST_NAME}:4444/wd/hub"


@pytest.fixture
def server_url():
    return f"https://{settings.APP_VIRTUAL_HOST_NAME}"


@pytest.fixture
def web_driver(selenium_hub_url):
    caps = {"browserName": settings.BROWSER, "acceptInsecureCerts": True}
    driver = webdriver.Remote(command_executor=selenium_hub_url, desired_capabilities=caps)

    yield driver

    driver.quit()
