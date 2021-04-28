from urllib.parse import urlparse

from django.urls import reverse
from selenium.webdriver.remote.webdriver import WebDriver

from {{cookiecutter.project_slug}}.tests.functional.utils import wait


class PasswordResetConfirmPage:
    def __init__(self, web_client: WebDriver) -> None:
        self.client = web_client

    def change_password(self, new_password1: str, new_password2: str = None) -> None:
        self._input_text(new_password1, "id_password1")
        self._input_text(new_password2 or new_password1, "id_password2")
        self._submit()

        self._assert_password_reset_complete()

    @wait
    def _input_text(self, text: str, _id: str) -> None:
        element = self.client.find_element_by_id(_id)
        element.send_keys(text)

    @wait
    def _submit(self) -> None:
        self.client.find_element_by_xpath('//input[@type="submit"]').click()

    @wait
    def _assert_password_reset_complete(self):
        assert urlparse(self.client.current_url).path == reverse("account_reset_password_from_key_done")
