from drf_spectacular.contrib.rest_auth import get_token_serializer_class
from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status

from {{cookiecutter.project_slug}}.core.serializers import (
    DetailResponseSerializer,
    NonFieldErrorResponseSerializer,
)


class LoginSchema(OpenApiViewExtension):
    target_class = "dj_rest_auth.views.LoginView"
    priority = 1

    def view_replacement(self):
        from {{cookiecutter.project_slug}}.users.api.serializers import LoginSerializer

        class Fixed(self.target_class):
            @extend_schema(
                operation_id="login",
                request={"application/json": LoginSerializer},
                responses={
                    status.HTTP_200_OK: OpenApiResponse(
                        get_token_serializer_class(),
                        description="Successful login",
                        examples=[
                            OpenApiExample(
                                "Success",
                                value={"key": "491484b928d4e497ef3359a789af8ac204fc96db"},
                                status_codes=[f"{status.HTTP_200_OK}"],
                            )
                        ],
                    ),
                    status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                        NonFieldErrorResponseSerializer,
                        description="Invalid input",
                        examples=[
                            OpenApiExample(
                                "Invalid credentials",
                                value={"non_field_errors": "Unable to log in with provided credentials"},
                                status_codes=[f"{status.HTTP_400_BAD_REQUEST}"],
                            )
                        ],
                    ),
                    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Unauthorized",
                        examples=[
                            OpenApiExample(
                                "Invalid auth header",
                                description="Attempting to login with the Authorization header already set",
                                value={"detail": "Invalid Token."},
                                status_codes=[f"{status.HTTP_401_UNAUTHORIZED}"],
                            )
                        ],
                    ),
                },
                tags=["auth"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


class LogoutSchema(OpenApiViewExtension):
    target_class = "dj_rest_auth.views.LogoutView"
    priority = 1

    def view_replacement(self):
        from django.conf import settings

        if getattr(settings, "ACCOUNT_LOGOUT_ON_GET", None):
            get_schema_params = {"responses": DetailResponseSerializer}
        else:
            get_schema_params = {"exclude": True}

        class Fixed(self.target_class):
            @extend_schema(operation_id="logout", **get_schema_params, tags=["auth"])
            def get(self, request, *args, **kwargs):
                pass

            @extend_schema(
                operation_id="logout",
                request=None,
                responses={
                    status.HTTP_200_OK: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Success",
                        examples=[
                            OpenApiExample(
                                "Success",
                                value={"detail": "Successfully logged out."},
                                status_codes=[f"{status.HTTP_200_OK}"],
                            )
                        ],
                    ),
                    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Unauthorized",
                        examples=[
                            OpenApiExample(
                                "No token",
                                value={"detail": "Invalid token header. No credentials provided."},
                                status_codes=[f"{status.HTTP_401_UNAUTHORIZED}"],
                            )
                        ],
                    ),
                },
                tags=["auth"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


class PasswordChangeSchema(OpenApiViewExtension):
    target_class = "dj_rest_auth.views.PasswordChangeView"
    priority = 1

    def view_replacement(self):
        from dj_rest_auth.serializers import PasswordChangeSerializer

        class Fixed(self.target_class):
            @extend_schema(
                operation_id="change_password",
                request={"application/json": PasswordChangeSerializer},
                responses={
                    status.HTTP_200_OK: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Success",
                        examples=[
                            OpenApiExample(
                                "Successful password change",
                                value={"detail": "New password has been saved."},
                                status_codes=[f"{status.HTTP_200_OK}"],
                            )
                        ],
                    ),
                    status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                        PasswordChangeSerializer,
                        description="Invalid input",
                        examples=[
                            OpenApiExample(
                                "Password too common",
                                value={"new_password2": "This password is too common."},
                                status_codes=[f"{status.HTTP_400_BAD_REQUEST}"],
                            )
                        ],
                    ),
                    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Unauthorized",
                        examples=[
                            OpenApiExample(
                                "No token",
                                description="Invalid or missing Authorization header",
                                value={"detail": "Authentication credentials were not provided."},
                                status_codes=[f"{status.HTTP_401_UNAUTHORIZED}"],
                            )
                        ],
                    ),
                },
                tags=["auth"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


class PasswordResetSchema(OpenApiViewExtension):
    target_class = "dj_rest_auth.views.PasswordResetView"
    priority = 1

    def view_replacement(self):
        from {{cookiecutter.project_slug}}.users.api.serializers import PasswordResetSerializer

        class Fixed(self.target_class):
            @extend_schema(
                operation_id="reset_password",
                request={"application/json": PasswordResetSerializer},
                responses={
                    status.HTTP_200_OK: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Success",
                        examples=[
                            OpenApiExample(
                                "Success",
                                value={"detail": "Password reset e-mail has been sent."},
                                status_codes=[f"{status.HTTP_200_OK}"],
                            )
                        ],
                    ),
                    status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                        PasswordResetSerializer,
                        description="Invalid input",
                        examples=[
                            OpenApiExample(
                                "User with email doesn't exist",
                                value={"email": "The e-mail address is not assigned to any user account"},
                                status_codes=[f"{status.HTTP_400_BAD_REQUEST}"],
                            )
                        ],
                    ),
                    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Unauthorized",
                        examples=[
                            OpenApiExample(
                                "Invalid auth header",
                                description="Attempting to reset password with the Authorization header already set",
                                value={"detail": "Invalid token."},
                                status_codes=[f"{status.HTTP_401_UNAUTHORIZED}"],
                            )
                        ],
                    ),
                },
                tags=["auth"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


class PasswordResetConfirmSchema(OpenApiViewExtension):
    target_class = "dj_rest_auth.views.PasswordResetConfirmView"
    priority = 1

    def view_replacement(self):
        from dj_rest_auth.serializers import PasswordResetConfirmSerializer

        class Fixed(self.target_class):
            @extend_schema(
                operation_id="reset_password_confirm",
                request={"application/json": PasswordResetConfirmSerializer},
                responses={
                    status.HTTP_200_OK: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Success",
                        examples=[
                            OpenApiExample(
                                "Successful password reset",
                                value={"detail": "Password has been reset with the new password."},
                            )
                        ],
                    ),
                    status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                        PasswordResetConfirmSerializer,
                        description="Invalid input",
                        examples=[
                            OpenApiExample(
                                "Invalid uid",
                                value={"uid": "Invalid value"},
                                status_codes=[f"{status.HTTP_400_BAD_REQUEST}"],
                            )
                        ],
                    ),
                },
                tags=["auth"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


class RegisterSchema(OpenApiViewExtension):
    target_class = "dj_rest_auth.registration.views.RegisterView"
    priority = 1

    def view_replacement(self):
        from allauth.account.app_settings import (
            EMAIL_VERIFICATION,
            EmailVerificationMethod,
        )

        from {{cookiecutter.project_slug}}.users.api.serializers import RegisterSerializer

        if EMAIL_VERIFICATION == EmailVerificationMethod.MANDATORY:
            response_serializer = DetailResponseSerializer
        else:
            response_serializer = get_token_serializer_class()

        class Fixed(self.target_class):
            @extend_schema(
                operation_id="register",
                request={"application/json": RegisterSerializer},
                responses={
                    status.HTTP_200_OK: OpenApiResponse(
                        response_serializer,
                        description="successful operation",
                        examples=[
                            OpenApiExample(
                                "Successful registration",
                                value={"detail": "Verification e-mail sent."},
                                status_codes=[f"{status.HTTP_200_OK}"],
                            )
                        ],
                    ),
                    status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                        RegisterSerializer,
                        description="Invalid input",
                        examples=[
                            OpenApiExample(
                                "Invalid email",
                                value={"email": "Enter a valid email address."},
                                status_codes=[f"{status.HTTP_400_BAD_REQUEST}"],
                            ),
                            OpenApiExample(
                                "Invalid password",
                                value={"password2": "This password is too common."},
                                status_codes=[f"{status.HTTP_400_BAD_REQUEST}"],
                            ),
                        ],
                    ),
                    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Unauthorized",
                        examples=[
                            OpenApiExample(
                                "Invalid auth header",
                                description="Attempting to register with the Authorization header already set",
                                value={"detail": "Invalid token."},
                                status_codes=[f"{status.HTTP_401_UNAUTHORIZED}"],
                            )
                        ],
                    ),
                },
                tags=["auth"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


class VerifyEmailSchema(OpenApiViewExtension):
    target_class = "dj_rest_auth.registration.views.VerifyEmailView"
    priority = 1

    def view_replacement(self):
        from dj_rest_auth.registration.serializers import VerifyEmailSerializer

        class Fixed(self.target_class):
            @extend_schema(
                operation_id="verify_email",
                request={"application/json": VerifyEmailSerializer},
                responses={
                    status.HTTP_200_OK: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Success",
                        examples=[OpenApiExample("Successful email verification", value={"detail": "ok"})],
                    ),
                    status.HTTP_404_NOT_FOUND: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Not found",
                        examples=[OpenApiExample("Invalid key", value={"detail": "Not found."})],
                    ),
                },
                tags=["auth"],
            )
            def post(self, request, *args, **kwargs):
                pass

        return Fixed


class UserDetailsSchema(OpenApiViewExtension):
    target_class = "dj_rest_auth.views.UserDetailsView"
    priority = 1

    def view_replacement(self):
        from {{cookiecutter.project_slug}}.users.api.serializers import UserSerializer

        class Fixed(self.target_class):
            @extend_schema(
                operation_id="get_user",
                description="Returns the user information for the currently logged on user.",
                responses={
                    status.HTTP_200_OK: UserSerializer,
                    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Unauthorized",
                        examples=[
                            OpenApiExample(
                                "No token",
                                value={"detail": "Invalid token."},
                                status_codes=[f"{status.HTTP_401_UNAUTHORIZED}"],
                            )
                        ],
                    ),
                },
                tags=["users"],
            )
            def get(self, *args, **kwargs):
                pass

            @extend_schema(
                operation_id="update_user",
                description="Updates the user information for the currently logged on user.",
                request={"application/json": UserSerializer},
                responses={
                    status.HTTP_200_OK: UserSerializer,
                    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Unauthorized",
                        examples=[
                            OpenApiExample(
                                "No token",
                                value={"detail": "Invalid token."},
                                status_codes=[f"{status.HTTP_401_UNAUTHORIZED}"],
                            )
                        ],
                    ),
                },
                tags=["users"],
            )
            def put(self, *args, **kwargs):
                pass

            @extend_schema(
                operation_id="partial_update_user",
                description="Partially updates the user information for the currently logged on user.",
                request={"application/json": UserSerializer},
                responses={
                    status.HTTP_200_OK: UserSerializer,
                    status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                        DetailResponseSerializer,
                        description="Unauthorized",
                        examples=[
                            OpenApiExample(
                                "No token",
                                value={"detail": "Invalid token."},
                                status_codes=[f"{status.HTTP_401_UNAUTHORIZED}"],
                            )
                        ],
                    ),
                },
                tags=["users"],
            )
            def patch(self, *args, **kwargs):
                pass

        return Fixed
