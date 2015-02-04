from rest_framework import authentication, permissions, viewsets
from .serializers import BrandSerializer

from .models import Brand


class DefaultsMixin(object):
    """Default settings for view authentication, permissions and pagination"""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class BrandViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint allowing brands to be viewed
    """
    queryset = Brand.published.all()
    serializer_class = BrandSerializer
