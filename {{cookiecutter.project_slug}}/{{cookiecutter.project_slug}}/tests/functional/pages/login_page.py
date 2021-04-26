import swagger_client

from .base_api_page import BaseAPIPage, api_call


class LoginPage(BaseAPIPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.client = swagger_client.AuthApi(self.api_client)
        self.api_key = None

    @api_call
    def login(self, email: str, password: str) -> None:
        data = {"email": email, "password": password}
        response = self.client.login(body=data)
        self.api_key = response.key
