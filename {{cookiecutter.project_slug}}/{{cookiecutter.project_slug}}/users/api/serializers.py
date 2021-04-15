{% if cookiecutter.user.username_field == "email" -%}
from dj_rest_auth.registration.serializers import (
    RegisterSerializer as RestAuthRegisterSerializer,
)
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
{% endif -%}
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["{{cookiecutter.user.username_field}}", "name", "url"]
        extra_kwargs = {
            "url": {
                "view_name": "api:user-detail",
                "lookup_field": "{{cookiecutter.user.slug_field}}",
            }
        }
{% if cookiecutter.user.username_field == "email" %}

class LoginSerializer(RestAuthLoginSerializer):
    username = None


class RegisterSerializer(RestAuthRegisterSerializer):
    username = None
    name = serializers.CharField()

    def get_cleaned_data(self):
        return {
            "name": self.validated_data.get("name", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }
{% endif %}