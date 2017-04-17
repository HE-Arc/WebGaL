from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^project/([0-9a-zA-Z\s-]*)/$', views.project, name='project'),
                  url(r'^upload/([0-9a-zA-Z\s-]*)/$', views.upload, name='upload'),
                  url(r'^profile/([0-9a-zA-Z\s-]*)/$', views.profile, name='profile'),
                  url(r'^comments/posted/$', views.comment_posted),
                  url(r'^comments/', include('django_comments.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT+'/media/')
