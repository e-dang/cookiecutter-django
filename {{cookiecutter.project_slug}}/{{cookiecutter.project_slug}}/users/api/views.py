from django.contrib.auth import get_user_model
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "{{cookiecutter.user.slug_field}}"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)
