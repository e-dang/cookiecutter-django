import pytest
import swagger_client
from swagger_client.rest import ApiException

from .base_api_page import BaseAPIPage, api_call


class UserSettingsPage(BaseAPIPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_client = swagger_client.UsersApi(self.api_client)
        self.auth_client = swagger_client.AuthApi(self.api_client)

    def assert_displays_info_for_user(self, user: dict) -> None:
        user_info = self._get_user_info()
        {% if cookiecutter.user.username_field == "username" -%}
        assert user_info.username == user["username"]
        {% endif -%}
        assert user_info.email == user["email"]
        assert user_info.name == user["name"]

    @api_call
    def change_password(self, old_credentials: dict, new_password1: str, new_password2: str = None) -> None:
        data = {
            "old_password": old_credentials["password"],
            "new_password1": new_password1,
            "new_password2": new_password2 or new_password1,
        }
        response = self.auth_client.change_password(data)

        assert response.detail == "New password has been saved."

    @api_call
    def logout(self) -> None:
        response = self.auth_client.logout()

        assert response.detail == "Successfully logged out."
        with pytest.raises(ApiException) as e:
            self.user_client.get_user()
            assert e.status == 401
            assert e.reason == "Unauthorized"

    @api_call
    def _get_user_info(self) -> swagger_client.User:
        return self.user_client.get_user()
