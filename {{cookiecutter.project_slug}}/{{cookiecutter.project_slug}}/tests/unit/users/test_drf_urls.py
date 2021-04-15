import pytest
from django.urls import resolve, reverse

from {{ cookiecutter.project_slug }}.users.models import User

pytestmark = pytest.mark.django_db


def test_user_detail(user: User):
    assert (
        reverse("api:user-detail", kwargs={"{{cookiecutter.user.slug_field}}": user.{{cookiecutter.user.slug_field}}})
        == f"/api/users/{user.{{cookiecutter.user.slug_field}}}/"
    )
    assert resolve(f"/api/users/{user.{{cookiecutter.user.slug_field}}}/").view_name == "api:user-detail"


def test_user_list():
    assert reverse("api:user-list") == "/api/users/"
    assert resolve("/api/users/").view_name == "api:user-list"


def test_user_me():
    assert reverse("api:user-me") == "/api/users/me/"
    assert resolve("/api/users/me/").view_name == "api:user-me"


def test_login():
    assert reverse("api:rest_login") == "/api/login/"
    assert resolve("/api/login/").view_name == "api:rest_login"


def test_logout():
    assert reverse("api:rest_logout") == "/api/logout/"
    assert resolve("/api/logout/").view_name == "api:rest_logout"


def test_password_reset():
    assert reverse("api:rest_password_reset") == "/api/password/reset/"
    assert resolve("/api/password/reset/").view_name == "api:rest_password_reset"


def test_password_reset_confirm():
    assert reverse("api:rest_password_reset_confirm") == "/api/password/reset/confirm/"
    assert resolve("/api/password/reset/confirm/").view_name == "api:rest_password_reset_confirm"


def test_password_change():
    assert reverse("api:rest_password_change") == "/api/password/change/"
    assert resolve("/api/password/change/").view_name == "api:rest_password_change"


def test_dj_rest_auth_user_detail():
    assert reverse("api:rest_user_details") == "/api/user/"
    assert resolve("/api/user/").view_name == "api:rest_user_details"


def test_register():
    assert reverse("api:rest_register") == "/api/registration/"
    assert resolve("/api/registration/").view_name == "api:rest_register"


def test_verify_email():
    assert reverse("api:rest_verify_email") == "/api/registration/verify-email/"
    assert resolve("/api/registration/verify-email/").view_name == "api:rest_verify_email"
