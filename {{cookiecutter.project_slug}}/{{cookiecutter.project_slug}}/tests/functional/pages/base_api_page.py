from typing import Any, Callable

import pytest
import swagger_client
from swagger_client.rest import ApiException


def api_call(func: Callable) -> Callable:
    def _inner(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except ApiException as e:
            pytest.fail(msg=str(e))

    return _inner


class BaseAPIPage:
    def __init__(self, host: str, api_key: str = None, ssl_ca_cert: str = None) -> None:
        self.configuration = swagger_client.Configuration()
        self.configuration.host = host

        if api_key is not None:
            self.configuration.api_key["Authorization"] = api_key
            self.configuration.api_key_prefix["Authorization"] = "Token"

        self.configuration.ssl_ca_cert = ssl_ca_cert
        self.api_client = swagger_client.ApiClient(self.configuration)
