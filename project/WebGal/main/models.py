from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    directory = models.SlugField()


class User(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    projects = models.IntegerField(default=0)
    email = models.EmailField()


class Comment(models.Model):
    pub_date = models.DateTimeField('date published')
    text = models.CharField(max_length=1000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
