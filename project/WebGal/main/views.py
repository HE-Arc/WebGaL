from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the WebGal index.")
	
def project(request):
    return HttpResponse("You're viewing a project.")
	
def login(request):
    return HttpResponse("You can login here.")
	
def upload(request):
    return HttpResponse("You can upload a project here.")
	