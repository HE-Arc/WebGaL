from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from .models import Project


def index(request):
    allprojects = Project.objects.all().order_by('-pub_date')
    context = {"allprojects": allprojects}
    return render(request, 'index.html', context)


def project(request):
    return HttpResponse("You're viewing a project.")


def upload(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


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
