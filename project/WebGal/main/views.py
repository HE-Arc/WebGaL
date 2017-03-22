from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

	
def project(request):
    return HttpResponse("You're viewing a project.")
	
def login(request):
    return HttpResponse("You can login here.")
	
def upload(request):
    return HttpResponse("You can upload a project here.")
	