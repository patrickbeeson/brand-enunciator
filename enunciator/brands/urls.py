from rest_framework import routers

from django.conf.urls import url, include

from .views import BrandViewSet

router = routers.DefaultRouter()
router.register(r'brands', views.BrandViewSet)

urlpatterns = [
    url(r'^', incude(router.urls))
]
