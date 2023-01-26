from typing import Optional, Any

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserManager(UserManager):
    def create_superuser(
        self,
        email: str,
        password: Optional[str],
        username: Optional[str] = None,
        **extra_fields: Any
    ):
        if not username:
            username = email
        return super().create_superuser(
            username,
            email,
            password,
            **extra_fields
        )


class User(AbstractUser):
    """
    User model
    """
    email = models.EmailField(_("email address"), unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
