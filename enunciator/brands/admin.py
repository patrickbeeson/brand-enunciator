from django.contrib import admin

from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Brand, BrandAdmin)
