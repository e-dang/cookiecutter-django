from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        if not email:
            raise ValueError(_("A user must have an email"))

        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)

        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))

        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self._create_user(email, password, **kwargs)
