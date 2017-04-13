from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from .models import Project
from django.contrib.auth.models import User


def index(request):
    allprojects = Project.objects.all().order_by('-pub_date')
    context = {"allprojects": allprojects}
    return render(request, 'index.html', context)


def project(request, projectname):
    context = {"projectname": projectname}
    return render(request, 'project.html', context)


def upload(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def profile(request, username):
    userid = User.objects.get(username=username)
    userprojects = Project.objects.filter(user=userid).order_by('-pub_date')
    context = {"userprojects": userprojects}
    return render(request, 'profile.html', context)


def projectiframe(request, projectname):
    templatelocation = Project.objects.get(project_name=projectname).location
    return loader.get_template(projectname)


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                self.handle_uploaded_file(f, request.POST.get('project_name'), request.POST.get('username'))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    @staticmethod
    def handle_uploaded_file(file, name, username):
        with open('static/projects/' + username + '/' + name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
