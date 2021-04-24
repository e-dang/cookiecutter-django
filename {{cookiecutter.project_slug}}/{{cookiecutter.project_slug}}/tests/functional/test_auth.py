from pytest_bdd import given, scenarios, then, when

from .pages.register_page import RegisterPage

scenarios("features/auth.feature")


@given("I am on the register screen", target_fixture="register_screen")
def register_screen(server_url: str) -> RegisterPage:
    return RegisterPage(server_url)


@given("I have valid registration information", target_fixture="registration_info")
def valid_info(valid_registration_info: dict) -> dict:
    return valid_registration_info


@when("I submit my information")
def submit_register_info(register_screen: RegisterPage, registration_info: dict) -> None:
    register_screen.register(registration_info)


@then("I am successfully logged in")
def confirm_logged_in(register_screen):
    register_screen.assert_successful_registration_request()
