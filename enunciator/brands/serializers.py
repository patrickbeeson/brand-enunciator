from rest_framework.serializers import ModelSerializer

from .models import Brand


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
