from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'full_name', 'primary_mobile', 'user_role', 'is_staff', 'is_active')
    list_filter = ('user_role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'primary_mobile', 'email')}),
        ('Permissions', {'fields': ('user_role', 'is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'primary_mobile', 'password1', 'password2', 'user_role', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'full_name', 'primary_mobile')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
