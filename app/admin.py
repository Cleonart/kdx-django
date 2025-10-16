from django.contrib import admin
from app.models import Company
from authentication.models import AuthUserCompany

Company._meta.verbose_name_plural = 'Companies / Tenants'
AuthUserCompany._meta.verbose_name_plural = 'User Organization Member'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'created_at', 'updated_at')
    search_fields = ('code', 'name')
    list_filter = ('created_at',)
    ordering = ('name',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Companies / Tenants'
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(AuthUserCompany)
class AuthUserCompanyAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'company_code', 'is_active')
    search_fields = (
        'user__username', 'user__email',
        'company__name', 'company__code')
    list_filter = ('company',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'User Organization Member'
        return super().changelist_view(request, extra_context=extra_context)
