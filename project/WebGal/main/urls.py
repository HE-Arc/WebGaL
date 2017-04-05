from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project', views.project, name='project'),
    url(r'^upload', views.FileFieldView.as_view(), name='upload'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
