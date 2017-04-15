from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from .models import Project
from .forms import UploadProject
from django.contrib.auth.models import User


def index(request):
    allprojects = Project.objects.all().order_by('-pub_date')
    context = {"allprojects": allprojects}
    return render(request, 'index.html', context)


def project(request, projectname):
    context = {"projectname": projectname}
    return render(request, 'project.html', context)


def upload(request, username):
    if request.method == 'POST':
        form = UploadProject(request.POST, request.FILES)
        if form.is_valid():
            project = Project(project_name=request.POST.get('project_name'),
                              pub_date=timezone.now(),
                              likes=0,
                              shares=0,
                              description=request.POST.get('description'),
                              image=(request.user.id, request.POST.get('project_name'), request.FILES.get('image')),
                              files=(
                              request.user.id, request.POST.get('project_name'), request.FILES.get('attachements')),
                              user=request.user.id)
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


def projectiframe(request, projectname):
    templatelocation = Project.objects.get(project_name=projectname).location
    return loader.get_template(projectname)
