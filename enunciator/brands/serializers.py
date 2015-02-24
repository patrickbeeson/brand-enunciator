from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """Brand serializer"""
    status_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'created',
            'website',
            'logo',
            'video',
            'video_thumbnail',
            'links',
            'status_display',
            'video_views',
        )

    def get_status_display(self, obj):
        """Return status using get_foo_display method from Django"""
        return obj.get_status_display()

    def get_links(self, obj):
        """Returns URI for object into the links field"""
        request = self.context['request']
        return {
            'self': reverse(
                'brand-detail',
                kwargs={'slug': obj.slug},
                request=request,
            )
        }
