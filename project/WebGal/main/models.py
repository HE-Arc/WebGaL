from django.db import models
from django.conf import settings


def upload_to(instance, filename):
    return settings.MEDIA_ROOT + '/media/%s/%s/%s' % (instance.user.id, instance.project_name, filename)


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    description = models.TextField(max_length=4000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=upload_to)
    files = models.FileField(upload_to=upload_to)


class Comment(models.Model):
    pub_date = models.DateTimeField('date published')
    text = models.CharField(max_length=1000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ProjectLikeUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('project', 'user',)
