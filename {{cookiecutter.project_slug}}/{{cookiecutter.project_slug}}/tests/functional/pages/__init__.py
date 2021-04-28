from .base_api_page import BaseAPIPage
from .inbox_page import InboxPage, MailHogServer, SMTPServer
from .login_page import LoginPage
from .password_reset_confirm_page import PasswordResetConfirmPage
from .password_reset_page import PasswordResetPage
from .register_page import RegisterPage
from .user_settings_page import UserSettingsPage

__all__ = [
    BaseAPIPage,
    InboxPage,
    MailHogServer,
    SMTPServer,
    LoginPage,
    PasswordResetPage,
    PasswordResetConfirmPage,
    RegisterPage,
    UserSettingsPage,
]
