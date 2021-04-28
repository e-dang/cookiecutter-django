import swagger_client

from .base_api_page import BaseAPIPage


class PasswordResetPage(BaseAPIPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.client = swagger_client.AuthApi(self.api_client)

    def request_password_reset(self, email: str) -> None:
        data = {"email": email}
        self.clear_auth_token()  # request will fail if sent with an auth token attached
        response = self.client.reset_password(data)
        assert response.detail == "Password reset e-mail has been sent."
