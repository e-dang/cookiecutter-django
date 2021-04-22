from {{ cookiecutter.project_slug }}.tests.assertions import assert_correct_url
from {{ cookiecutter.project_slug }}.tests.factories import UserFactory


def test_user_detail(user_factory: UserFactory):
    kwargs = {"uuid": user_factory.build().uuid}
    assert_correct_url("api:user-detail", "/api/users/{uuid}/", kwargs)


def test_user_list():
    assert_correct_url("api:user-list", "/api/users/")


def test_login():
    assert_correct_url("api:rest_login", "/api/login/")


def test_logout():
    assert_correct_url("api:rest_logout", "/api/logout/")


def test_password_reset():
    assert_correct_url("api:rest_password_reset", "/api/password/reset/")


def test_password_reset_confirm():
    assert_correct_url(
        "api:rest_password_reset_confirm", "/api/password/reset/confirm/"
    )


def test_password_change():
    assert_correct_url("api:rest_password_change", "/api/password/change/")


def test_dj_rest_auth_user_detail():
    assert_correct_url("api:rest_user_details", "/api/user/")


def test_register():
    assert_correct_url("api:rest_register", "/api/registration/")


def test_verify_email():
    assert_correct_url("api:rest_verify_email", "/api/registration/verify-email/")
