"""
Module for all Form Tests.
"""
import pytest
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.users.forms import UserCreationForm
from {{ cookiecutter.project_slug }}.users.models import User

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
    """
    Test class for all tests related to the UserCreationForm
    """

    def test_{{cookiecutter.user.username_field}}_validation_error_msg(self, user: User):
        """
        Tests UserCreation Form's unique validator functions correctly by testing:
            1) A new user with an existing {{cookiecutter.user.username_field}} cannot be added.
            2) Only 1 error is raised by the UserCreation Form
            3) The desired error message is raised
        """

        # The user already exists,
        # hence cannot be created.
        form = UserCreationForm(
            {
                "{{cookiecutter.user.username_field}}": user.{{cookiecutter.user.username_field}},
                "password1": user.password,
                "password2": user.password,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "{{cookiecutter.user.username_field}}" in form.errors
        assert form.errors["{{cookiecutter.user.username_field}}"][0] == _("This {{cookiecutter.user.username_field}} has already been taken.")
