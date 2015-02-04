from django.conf.urls import patterns, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

from brands.urls import router
from .views import IndexTemplateView

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(brands.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexTemplateView, name='home'),
]
