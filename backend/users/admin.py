from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_player', 'is_staff')
    list_filter = ('role', 'is_player', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
         'fields': ('role', 'is_player', 'avatar', 'bio')}),
    )
