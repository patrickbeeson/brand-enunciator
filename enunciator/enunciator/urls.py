from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexTemplateView

urlpatterns = patterns('',
    url(r'^$', IndexTemplateView, name='home'),
    url(r'^brands/', include('brands.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
