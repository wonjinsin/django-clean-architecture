from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, default=None)

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
