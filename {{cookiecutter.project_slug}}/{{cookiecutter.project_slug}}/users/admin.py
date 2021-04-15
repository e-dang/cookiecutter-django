from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        {% if cookiecutter.user.username_field == "username" -%}
        (None, {"fields": ("{{cookiecutter.user.slug_field}}", "password")}),
        {% else -%}
        (None, {"fields": ("password",)}),
        {% endif -%}
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    {% if cookiecutter.user.username_field == "email" -%}
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    {% endif -%}
    list_display = ["{{cookiecutter.user.username_field}}", "name",{% if cookiecutter.user.slug_field == "uuid" %} "uuid",{% endif %} "is_superuser"]
    search_fields = ["{{cookiecutter.user.username_field}}", "name"]
    ordering = ["{{cookiecutter.user.username_field}}"]
