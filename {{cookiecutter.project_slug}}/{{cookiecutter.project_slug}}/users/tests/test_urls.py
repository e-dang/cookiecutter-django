import pytest
from django.urls import resolve, reverse

from {{ cookiecutter.project_slug }}.users.models import User

pytestmark = pytest.mark.django_db


def test_detail(user: User):
    assert (
        reverse("users:detail", kwargs={"{{cookiecutter.user.slug_field}}": user.{{cookiecutter.user.slug_field}}})
        == f"/users/{user.{{cookiecutter.user.slug_field}}}/"
    )
    assert resolve(f"/users/{user.{{cookiecutter.user.slug_field}}}/").view_name == "users:detail"


def test_update():
    assert reverse("users:update") == "/users/~update/"
    assert resolve("/users/~update/").view_name == "users:update"


def test_redirect():
    assert reverse("users:redirect") == "/users/~redirect/"
    assert resolve("/users/~redirect/").view_name == "users:redirect"
