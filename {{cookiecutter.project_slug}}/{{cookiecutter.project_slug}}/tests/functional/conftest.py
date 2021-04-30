import subprocess

import pytest
from django.conf import settings
from selenium import webdriver


def build_docker_exec(**kwargs):
    env_vars = []
    for key, item in kwargs.items():
        env_vars.append("-e")
        env_vars.append(f"{key}={item}")
    return [
        "docker",
        "exec",
        *env_vars,
        "-e",
        f"TARGET_ENV={settings.TARGET_ENV}",
        "-i",
        settings.APP_HOST_NAME,
        "/bin/bash",
    ]


def execute_command(command, file_path):
    try:
        with open(file_path, "rb") as file:
            subprocess.run(command, stdin=file, check=True)
    except subprocess.CalledProcessError as e:
        pytest.fail(msg=str(e))


@pytest.fixture(autouse=True)
def reset_database():
    command = build_docker_exec()
    execute_command(command, "/flush")


@pytest.fixture
def verified_user(user_json: dict) -> dict:
    command = build_docker_exec(
        CLIENT_{{cookiecutter.user.username_field.upper()}}=user_json["{{cookiecutter.user.username_field}}"],
        CLIENT_PASSWORD=user_json["password"],
        CLIENT_NAME=user_json["name"],
        FLAGS="--verified",
    )
    execute_command(command, "/create_user")
    return user_json


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
def web_client(selenium_hub_url):
    caps = {"browserName": settings.BROWSER, "acceptInsecureCerts": True}
    driver = webdriver.Remote(command_executor=selenium_hub_url, desired_capabilities=caps)

    yield driver

    driver.quit()
