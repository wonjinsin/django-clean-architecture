from django.contrib import admin
from model.account.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
