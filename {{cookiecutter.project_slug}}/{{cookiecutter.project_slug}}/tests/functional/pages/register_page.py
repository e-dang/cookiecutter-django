import swagger_client

from .base_api_page import BaseAPIPage, api_call


class RegisterPage(BaseAPIPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.client = swagger_client.AuthApi(self.api_client)

    @api_call
    def register(self, info: dict) -> swagger_client.Register:
        return self.client.register(info)
