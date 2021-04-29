from django.conf import settings
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from {{cookiecutter.project_slug}}.users.api.views import UserViewSet

app_name = "api"


router = SimpleRouter()
router.register("users", UserViewSet)

paths = router.urls
paths += [
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
]

if "drf_spectacular" in settings.INSTALLED_APPS:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    paths += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="api:v1:schema"), name="swagger-ui"),
    ]

urlpatterns = [path("v1/", include((paths, "v1")))]
