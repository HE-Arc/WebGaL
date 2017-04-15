from django.shortcuts import render
from django.utils import timezone
from .models import Project
from .forms import UploadProject
from django.conf import settings
from django.contrib.auth.models import User
import os
import zipfile


def index(request):
    allprojects = Project.objects.all().order_by('-pub_date')
    context = {"allprojects": allprojects}
    return render(request, 'index.html', context)


def project(request, projectname):
    context = {"projectname": projectname, "username": request.user}
    return render(request, 'project.html', context)


def handle_project_files(files, username, projectname):
    directory = settings.MEDIA_ROOT + '/' + username + '/' + projectname
    if not os.path.exists(directory):
        os.makedirs(directory)
    zip_ref = zipfile.ZipFile(directory, 'r')
    zip_ref.extractall(directory)
    zip_ref.close()


def upload(request, username):
    if request.method == 'POST':
        form = UploadProject(request.POST, request.FILES)
        if form.is_valid():
            handle_project_files(request.FILES.get('attachements'), request.user, request.POST.get('project_name'))
            project = Project(project_name=request.POST.get('project_name'),
                              pub_date=timezone.now(),
                              likes=0,
                              shares=0,
                              description=request.POST.get('description'),
                              image=(request.user, request.POST.get('project_name'), request.FILES.get('image')),
                              user=request.user)
            project.save()
            return render(request, 'profile.html', {"username": username})
        else:
            return render(request, 'upload.html', {'form': form, "username": username})
    else:
        form = UploadProject()
        return render(request, 'upload.html', {'form': form, "username": username})


def profile(request, username):
    userid = User.objects.get(username=username)
    userprojects = Project.objects.filter(user=userid).order_by('-pub_date')
    context = {"userprojects": userprojects, "username": username}
    return render(request, 'profile.html', context)
