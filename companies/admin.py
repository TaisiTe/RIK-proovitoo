from django.contrib import admin
from .models import Company, Shareholder


class ShareholderInline(admin.StackedInline):
    model = Shareholder
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'reg_code', 'date_founded', 'total_capital']}),
    ]
    inlines = [ShareholderInline]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Shareholder)
