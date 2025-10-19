from authentication.models import AuthUserCompany, AuthGroupCompany
from app.models import Company
from django.contrib import admin


Company._meta.verbose_name_plural = 'Companies / Tenants'
AuthUserCompany._meta.verbose_name_plural = 'User Organization Member'
AuthGroupCompany._meta.verbose_name_plural = 'Group Organization Member'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'created_at', 'updated_at')
    search_fields = ('code', 'name')
    list_filter = ('created_at',)
    ordering = ('name',)


@admin.register(AuthUserCompany)
class AuthUserCompanyAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'is_active')
    search_fields = (
        'user__username', 'user__email',
        'company__name', 'company__code')
    list_filter = ('company',)


@admin.register(AuthGroupCompany)
class AuthGroupCompanyAdmin(admin.ModelAdmin):
    list_display = ('group', 'company', 'is_active')
    search_fields = (
        'group__name',
        'company__name', 'company__code')
    list_filter = ('company',)
