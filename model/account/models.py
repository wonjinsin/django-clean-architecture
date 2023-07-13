from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from util.logger import logger


class AccountManager(BaseUserManager):
    def create_user(self, email, password, name):
        logger.info('create_user')
        user = self.model(
            email=email,
            name=name,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name):
        user = self.model(
            email=email,
            name=name,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', max_length=50,
                              unique=True, null=False, default=None)
    password = models.CharField(
        'password', max_length=128, null=False)
    name = models.CharField('name', max_length=20, null=False, default=None)
    created_at = models.DateTimeField('created_at', auto_now=True)
    is_staff = models.BooleanField('is_staff', default=False)
    active = models.BooleanField('active', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AccountManager()

    class Meta:
        db_table = "account"
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def __str__(self):
        return self.email
