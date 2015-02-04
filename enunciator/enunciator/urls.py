from rest_framework.authtoken.views import obtain_auth_token

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from brands.urls import router

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
