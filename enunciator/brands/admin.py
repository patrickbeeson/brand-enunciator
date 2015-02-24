from django.contrib import admin

from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    readonly_fields = (
        'video_url',
        'video_thumbnail_url',
        'video_views',
    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
                'tagline',
                'description',
                'website',
                'logo',
                'vine_url',
                'video_views',
            )
        }),
        ('Status', {
            'fields': (
                'status',
                'status_changed',
            )
        }),
        ('Vine data', {
            'classes': ('collapse',),
            'fields': (
                'video_url',
                'video_thumbnail_url',
                'video',
                'video_thumbnail',
            )
        }),
    )

admin.site.register(Brand, BrandAdmin)
