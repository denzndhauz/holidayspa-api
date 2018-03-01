from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        app_label = "rest"
