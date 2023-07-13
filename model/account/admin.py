from django.contrib import admin
from model.account.models import Account
from django.contrib.auth.admin import UserAdmin


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'active',)
    list_filter = ('email', 'is_staff', 'active',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {
         'fields': ('is_staff', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'active', 'is_staff', 'is_superuser', 'user_permissions')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
