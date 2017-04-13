from django.db import models
from django.conf import settings


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    description = models.CharField(max_length=4000)
    image = models.ImageField()
    location = models.CharField(max_length=4000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    pub_date = models.DateTimeField('date published')
    text = models.CharField(max_length=1000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
