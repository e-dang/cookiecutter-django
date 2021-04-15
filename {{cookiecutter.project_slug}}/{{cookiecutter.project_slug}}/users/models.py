{% if cookiecutter.user.slug_field == "uuid" -%}
import uuid

{% endif -%}

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField{% if cookiecutter.user.username_field == "email" %}, EmailField{% endif %}{% if cookiecutter.user.slug_field == "uuid" -%}, UUIDField{% endif %}
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

{% if cookiecutter.user.username_field == "email" -%}
from .managers import UserManager

{% endif %}
class User(AbstractUser):
    """Default user for {{cookiecutter.project_name}}."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    {% if cookiecutter.user.slug_field == "uuid" -%}
    uuid = UUIDField(_("Public lookup id"), unique=True, default=uuid.uuid4, db_index=True, editable=False)
    {% endif -%}
    {% if cookiecutter.user.username_field == "email" -%}
    username = None
    email = EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    {% endif -%}

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"{{cookiecutter.user.slug_field}}": self.{{cookiecutter.user.slug_field}}})
