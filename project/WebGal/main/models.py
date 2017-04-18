from django.db import models
from django.conf import settings


def upload_to(instance, filename):
    return settings.MEDIA_ROOT + '/media/%s/%s/%s' % (instance.user.id, instance.project_name, filename)


def upload_image_to(instance, filename):
    return settings.MEDIA_ROOT + '/media/%s/%s/%s' % (instance.user.id, instance.project_name, 'thumbnail.jpg')


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=4000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=upload_image_to)
    files = models.FileField(upload_to=upload_to)

    def get_absolute_url(self):
        return "/project/Projet %i/" % self.id


class ProjectLikeUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'user',)
