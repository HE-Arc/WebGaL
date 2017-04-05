from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url('^', include('django.contrib.auth.urls')),
    url('^', include('registration.backends.hmac.urls')),
]
