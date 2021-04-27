import swagger_client

from .base_api_page import BaseAPIPage, api_call


class LoginPage(BaseAPIPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.client = swagger_client.AuthApi(self.api_client)
        self.auth_token = None

    @api_call
    def login(self, {{cookiecutter.user.username_field}}: str, password: str) -> None:
        data = {"{{cookiecutter.user.username_field}}": {{cookiecutter.user.username_field}}, "password": password}
        self.clear_auth_token()  # request will fail if sent with an auth token attached
        response = self.client.login(data)
        self.auth_token = response.key

    def clear_auth_token(self) -> None:
        super().clear_auth_token()
        self.auth_token = None
