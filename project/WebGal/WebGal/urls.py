from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url('^', include('django.contrib.auth.urls')),
    url('^', include('registration.backends.hmac.urls')),
]

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass

    urlpatterns += static.static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
