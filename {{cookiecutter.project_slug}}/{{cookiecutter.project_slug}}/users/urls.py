from django.urls import path

from {{ cookiecutter.project_slug }}.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    {% if cookiecutter.user.slug_field == "username" -%}
    path("<str:username>/", view=user_detail_view, name="detail"),
    {% else -%}
    path("<uuid:uuid>/", view=user_detail_view, name="detail"),
    {% endif -%}
]
