from functools import wraps

import pytest
import swagger_client
from swagger_client.rest import ApiException


def api_call(func):
    @wraps(func)
    def _inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiException as e:
            pytest.fail(msg=str(e))

    return _inner


class BaseAPIPage:
    def __init__(self, host: str, auth_token: str = None, ssl_ca_cert: str = None) -> None:
        self.configuration = swagger_client.Configuration()
        self.configuration.host = host

        if auth_token is not None:
            self.set_auth_token(auth_token)

        self.configuration.ssl_ca_cert = ssl_ca_cert
        self.api_client = swagger_client.ApiClient(self.configuration)

    def set_auth_token(self, token: str) -> None:
        self.configuration.api_key["Authorization"] = token
        self.configuration.api_key_prefix["Authorization"] = "Token"

    def clear_auth_token(self) -> None:
        self.configuration.api_key = {}
        self.configuration.api_key_prefix = {}
