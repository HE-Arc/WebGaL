from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^project/([0-9a-zA-Z\s-]*)/$', views.project, name='project'),
                  url(r'^upload/([0-9a-zA-Z\s-]*)/$', views.upload, name='upload'),
                  url(r'^profile/([0-9a-zA-Z\s-]*)/$', views.profile, name='profile'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

