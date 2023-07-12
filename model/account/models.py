from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now


class AccountManager(BaseUserManager):
    def create_user(self, username, email, password, fullname, is_staff):
        user = self.model(
            email=email,
            username=username,
            fullname=fullname,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, fullname, is_admin, is_staff):
        user = self.model(
            email=email,
            username=username,
            fullname=fullname,
            is_admin=is_admin,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('name', max_length=20, default=None)
    password = models.CharField('비밀번호', max_length=128, default=None)
    email = models.EmailField('이메일 주소', max_length=50,
                              unique=True, default=None)
    fullname = models.CharField('이름', max_length=20, default=None)
    join_date = models.DateTimeField('가입일', auto_now=True)
    is_staff = models.BooleanField('스태프', default=True)
    is_admin = models.BooleanField('어드민', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fullname', 'is_staff', 'is_admin']

    objects = AccountManager()

    class Meta:
        db_table = "account"
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
