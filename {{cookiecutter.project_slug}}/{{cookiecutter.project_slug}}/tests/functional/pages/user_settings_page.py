import swagger_client

from .base_api_page import BaseAPIPage, api_call


class UserSettingsPage(BaseAPIPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.client = swagger_client.UsersApi(self.api_client)

    @api_call
    def user_info(self) -> swagger_client.User:
        return self.client.get_user()
