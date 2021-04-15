from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        {% if cookiecutter.user.username_field == "email" -%}
        fields = ["email", "name", "password1", "password2"]
        {% endif -%}
        error_messages = {
            "{{cookiecutter.user.username_field}}": {"unique": _("This {{cookiecutter.user.username_field}} has already been taken.")}
        }
