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


@pytest.fixture
def user_settings_page(server_url: str, auth_token: str, ssl_ca_cert: str) -> UserSettingsPage:
    return UserSettingsPage(server_url, auth_token=auth_token, ssl_ca_cert=ssl_ca_cert)


@pytest.fixture
def auth_token(login_page: LoginPage) -> str:
    return login_page.auth_token


@pytest.fixture
def credentials() -> dict:
    return {"{{cookiecutter.user.username_field}}": None, "password": None}


@given("I am an unverified user", target_fixture="user")
def unverified_user(user_json: dict) -> dict:
    return user_json


@given("I am on the register page", target_fixture="register_page")
def register_page(server_url: str, ssl_ca_cert: str) -> RegisterPage:
    return RegisterPage(server_url, ssl_ca_cert=ssl_ca_cert)


@given("I have valid registration information", target_fixture="registration_info")
def valid_registration_info(valid_registration_info: dict, credentials: dict) -> dict:
    credentials["{{cookiecutter.user.username_field}}"] = valid_registration_info["{{cookiecutter.user.username_field}}"]
    credentials["password"] = valid_registration_info["password1"]
    return valid_registration_info


@when("I submit my information")
def submit_registration_info(register_page: RegisterPage, registration_info: dict) -> None:
    register_page.register(registration_info)


@when("I confirm my email address")
def confirm_email_address(inbox_page: InboxPage, registration_info: dict) -> None:
    inbox_page.confirm_email_address(registration_info["email"])


@given("I am on the login page")
@when("I go to the login page")
def on_login_page(login_page: LoginPage) -> None:
    pass


@when("I submit my credentials")
def submit_credentials(login_page: LoginPage, credentials: dict) -> None:
    login_page.login(**credentials)


@then("I am successfully logged in")
def confirm_logged_in(user_settings_page: UserSettingsPage, user: dict) -> None:
    user_settings_page.assert_displays_info_for_user(user)


################################################################################################


@given("I am a verified user", target_fixture="user")
def verified_user_(verified_user: dict) -> dict:
    return verified_user


@given("I have valid login credentials", target_fixture="credentials")
def valid_login_credentials(user: dict) -> None:
    return {"{{cookiecutter.user.username_field}}": user["{{cookiecutter.user.username_field}}"], "password": user["password"]}


@pytest.fixture
def new_password(credentials: dict) -> str:
    return credentials["password"] + "extra_chars123"


@when("I go to the user settings page")
def on_user_settings_page(user_settings_page: UserSettingsPage) -> None:
    pass


@when("I change my password")
def change_password(user_settings_page: UserSettingsPage, credentials: dict, new_password: str) -> None:
    user_settings_page.change_password(credentials, new_password)


@when("I logout")
def logout(user_settings_page: UserSettingsPage) -> None:
    user_settings_page.logout()


@when("I submit my new credentials")
def submit_new_credentials(
    login_page: LoginPage, user_settings_page: UserSettingsPage, credentials: dict, new_password: str
) -> None:
    login_page.login(credentials["{{cookiecutter.user.username_field}}"], new_password)
    user_settings_page.set_auth_token(login_page.auth_token)
