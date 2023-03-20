from importlib.resources import _

from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone

from datesConsult.managers import CustomUserManager


class CustomUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    # Use 'email' as username field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # define the user manager class for 'User'
    # Specified that all objects for the class come from
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")