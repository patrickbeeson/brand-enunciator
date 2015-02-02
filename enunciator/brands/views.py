from rest_framework.viewsets import ModelViewSet
from .serializers import BrandSerializer

from .models import Brand


class BrandViewSet(ModelViewSet):
    """
    API endpoint allowing brands to be viewed
    """
    queryset = Brand.published.all()
    serializer_class = BrandSerializer
