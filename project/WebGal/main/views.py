from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Project, ProjectLikeUser
from django_comments.models import Comment
from .forms import UploadProject, AddComment
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST

import os
import zipfile


def index(request):
    allprojects = Project.objects.all().order_by('-pub_date')
    if request.method == 'POST':
        if 'like' in request.POST:
            project_id = int(request.POST.get('project_id'))
            user_id = int(request.POST.get('user_id'))
            if not ProjectLikeUser.objects.filter(project_id=project_id, user_id=user_id).exists():
                project = Project.objects.get(pk=project_id)
                project.likes += 1
                project.save()

                projectLikeUser = ProjectLikeUser(project_id=project_id, user_id=user_id)
                projectLikeUser.save()
    context = {"allprojects": allprojects}
    return render(request, 'index.html', context)


@login_required
@require_POST
def like(request):
    project_id = int(request.POST.get('project_id'))
    user_id = int(request.POST.get('user_id'))
    if not ProjectLikeUser.objects.filter(project_id=project_id, user_id=user_id).exists():
        project = Project.objects.get(pk=project_id)
        project.likes += 1
        project.save()

        projectLikeUser = ProjectLikeUser(project_id=project_id, user_id=user_id)
        projectLikeUser.save()
    return HttpResponse()


def project(request, projectname):
    project = Project.objects.get(project_name=projectname)
    if request.method == 'POST':
        # Useless for now !!
        if 'deleteComment' in request.POST:
            comment_id = int(request.POST.get('comment_id'))
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
    context = {"project": project, "DEBUG": settings.DEBUG}
    return render(request, 'project.html', context)


def projectiframe(request, userid, project, *args):
    if 'media' not in settings.MEDIA_ROOT:
        path = settings.MEDIA_ROOT + '/media/' + userid + '/' + project
    else:
        path = settings.MEDIA_ROOT + '/' + userid + '/' + project
    if args[0] == '':
        return render(request, path + '/index.html')
    else:
        return render(request, path + '/' + args[0])


def comment_posted(request):
    if request.GET['c']:
        comment_id = request.GET['c']  # B
        comment = Comment.objects.get(pk=comment_id)
        project = Project.objects.get(id=comment.object_pk)  # C
        if project:
            return HttpResponseRedirect(project.get_absolute_url())  # D
    return HttpResponseRedirect("/")


def handle_project_files(user, projectname, files):
    if 'media' not in settings.MEDIA_ROOT:
        directory = settings.MEDIA_ROOT + '/media/' + str(user.id) + '/' + projectname
    else:
        directory = settings.MEDIA_ROOT + str(user.id) + '/' + projectname
    zip_ref = zipfile.ZipFile(directory + '/' + str(files), 'r')
    zip_ref.extractall(directory)
    zip_ref.close()
    os.remove(directory + '/' + str(files))


def upload(request, username):
    if request.method == 'POST':
        form = UploadProject(request.POST, request.FILES)
        if form.is_valid():
            project = Project(project_name=request.POST.get('project_name'),
                              pub_date=timezone.now(),
                              likes=0,
                              shares=0,
                              description=request.POST.get('description'),
                              image=request.FILES.get('image'),
                              files=request.FILES.get('attachments'),
                              user=request.user)
            project.save()
            print(request.FILES.get('attachments'))
            handle_project_files(request.user, request.POST.get('project_name'), request.FILES.get('attachments'))
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
