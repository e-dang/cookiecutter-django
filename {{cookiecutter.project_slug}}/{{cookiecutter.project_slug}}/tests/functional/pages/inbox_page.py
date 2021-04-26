from datetime import datetime

import requests
from rest_framework import status
from selenium.webdriver.remote.webdriver import WebDriver

from my_awesome_project.tests.utils import parse_url


class SMTPServer:
    def get_email(self, recipient_email: str) -> str:
        pass


class MailHogServer(SMTPServer):
    def __init__(self, host_url: str) -> None:
        self.host_url = host_url

    def get_email(self, recipient_email: str) -> str:
        url = self._build_url(recipient_email)
        response = requests.get(url)

        assert response.status_code == status.HTTP_200_OK

        emails = [item["Content"] for item in response.json()["items"]]
        emails = sorted(emails, key=lambda x: self._to_datetime(x["Headers"]["Date"][0]))
        return emails[0]["Body"]

    def _build_url(self, recipient_email: str) -> str:
        return self.host_url + f"/api/v2/search?kind=to&query={recipient_email}"

    def _to_datetime(self, date: str) -> datetime:
        return datetime.strptime(date, "%a, %d %b %Y %H:%M:%S -%f")


class InboxPage:
    def __init__(self, web_client: WebDriver, smtp_server: SMTPServer) -> None:
        self.web_client = web_client
        self.smtp_server = smtp_server

    def confirm_email_address(self, recipient_email: str) -> None:
        email = self.smtp_server.get_email(recipient_email)
        url = parse_url(email)
        self._go_to_confirmation_page(url)

    def _go_to_confirmation_page(self, url: str) -> None:
        self.web_client.get(url)
