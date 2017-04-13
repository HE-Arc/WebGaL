from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^project/([0-9a-zA-Z\s-]*)/$', views.project, name='project'),
                  url(r'^upload', views.FileFieldView.as_view(), name='upload'),
                  url(r'^profile/([0-9a-zA-Z\s-]*)/$', views.profile, name='profile'),
                  url(r'^projectiframe/([0-9a-zA-Z\s-]*)/$', views.projectiframe,
                      name='projectiframe')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
