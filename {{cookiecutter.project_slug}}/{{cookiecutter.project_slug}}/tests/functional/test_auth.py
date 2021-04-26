import pytest
from django.conf import settings
from pytest_bdd import given, scenarios, then, when
from selenium.webdriver.remote.webdriver import WebDriver

from .pages.inbox_page import InboxPage, MailHogServer, SMTPServer
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.user_settings_page import UserSettingsPage

scenarios("features/auth.feature")


@pytest.fixture
def smtp_server() -> SMTPServer:
    return MailHogServer(f"http://{settings.MAILHOG_HOST_NAME}:{settings.MAILHOG_PORT}")


@pytest.fixture
def inbox_page(web_driver: WebDriver, smtp_server: SMTPServer) -> InboxPage:
    return InboxPage(web_driver, smtp_server)


@pytest.fixture
def login_page(server_url: str, ssl_ca_cert: str) -> LoginPage:
    return LoginPage(server_url, ssl_ca_cert=ssl_ca_cert)


@given("I am on the register page", target_fixture="register_page")
def register_page(server_url: str, ssl_ca_cert: str) -> RegisterPage:
    return RegisterPage(server_url, ssl_ca_cert=ssl_ca_cert)


@given("I have valid registration information", target_fixture="registration_info")
def valid_info(valid_registration_info: dict) -> dict:
    return valid_registration_info


@when("I submit my information")
def submit_registration_info(register_page: RegisterPage, registration_info: dict) -> None:
    register_page.register(registration_info)


@when("I confirm my email address")
def confirm_email_address(inbox_page: InboxPage, registration_info: dict) -> None:
    inbox_page.confirm_email_address(registration_info["email"])


@when("I go to the login page")
def go_to_login_page(login_page: LoginPage) -> None:
    pass


@when("I submit my credentials")
def submit_credentials(login_page: LoginPage, registration_info: dict) -> None:
    login_page.login(registration_info["email"], registration_info["password1"])


@then("I am successfully logged in")
def confirm_logged_in(login_page: LoginPage, server_url: str, ssl_ca_cert: str, registration_info: dict) -> None:
    settings_page = UserSettingsPage(server_url, api_key=login_page.api_key, ssl_ca_cert=ssl_ca_cert)
    user_info = settings_page.user_info()  # should not raise
    assert user_info.email == registration_info["email"]
    assert user_info.name == registration_info["name"]
