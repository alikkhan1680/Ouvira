from django.contrib import admin

from apps.company.models import (
    Company,
    CompanySettings,
    Role,
    UserCompany,
    Invitation,
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'status',
        'created_by',
        'created_at',
    )
    list_filter = ('status',)
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'logo', 'address', 'status')
        }),
        ('Ownership', {
            'fields': ('created_by',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(CompanySettings)
class CompanySettingsAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'default_language',
        'default_currency',
        'timezone',
        'updated_at',
    )
    readonly_fields = ('updated_at',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_system_role', 'created_at')
    list_filter = ('is_system_role',)
    search_fields = ('name',)
    readonly_fields = ('created_at',)


@admin.register(UserCompany)
class UserCompanyAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'company',
        'role',
        'is_primary_company',
        'is_active',
        'joined_at',
    )
    list_filter = (
        'company',
        'role',
        'is_active',
        'is_primary_company',
    )
    search_fields = (
        'user__email',
        'company__name',
    )
    readonly_fields = ('joined_at',)

@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'company',
        'role',
        'status',
        'invited_by',
        'accepted_by',
        'expires_at',
        'created_at',
    )
    list_filter = ('status', 'company', 'role')
    search_fields = ('email',)
    readonly_fields = ('token', 'created_at')

    fieldsets = (
        ('Invitation Info', {
            'fields': ('company', 'email', 'role', 'status')
        }),
        ('Tracking', {
            'fields': ('token', 'expires_at')
        }),
        ('Audit', {
            'fields': ('invited_by', 'accepted_by', 'created_at')
        }),
    )

