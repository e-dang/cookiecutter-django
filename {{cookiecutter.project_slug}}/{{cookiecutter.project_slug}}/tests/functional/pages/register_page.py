import swagger_client
from django.conf import settings
from swagger_client.rest import ApiException


class RegisterPage:
    def __init__(self, host: str) -> None:
        self.configuration = swagger_client.Configuration()
        self.configuration.host = host
        self.configuration.ssl_ca_cert = f"{settings.ROOT_DIR}/certs/rootCA.pem"
        self.client = swagger_client.AuthApi(swagger_client.ApiClient(self.configuration))
        self.response = None

    def register(self, info: dict) -> None:
        try:
            self.response = self.client.register(info)
        except ApiException as e:
            self.response = e

    def assert_successful_registration_request(self):
        assert isinstance(self.response, swagger_client.RestAuthDetail)
