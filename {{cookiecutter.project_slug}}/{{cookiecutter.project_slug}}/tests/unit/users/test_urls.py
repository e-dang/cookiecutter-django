from {{ cookiecutter.project_slug }}.tests.assertions import assert_correct_url
from {{ cookiecutter.project_slug }}.tests.factories import UserFactory


def test_detail(user_factory: UserFactory):
    kwargs = {"uuid": user_factory.build().uuid}
    assert_correct_url("users:detail", "/users/{uuid}/", kwargs)


def test_update():
    assert_correct_url("users:update", "/users/~update/")


def test_redirect():
    assert_correct_url("users:redirect", "/users/~redirect/")
