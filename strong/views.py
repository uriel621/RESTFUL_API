from django.shortcuts import render
from strong.models import Project, Images
from django.conf import settings

settings.MEDIA_URL = '/media/' 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def strong(request):
    settings.MEDIA_URL = '/strong/images/'    
    project_model = Project.objects.order_by('type_of_project')
    images_model = Images.objects.order_by('image')
    projects = {'project_model':project_model, 'images_model':images_model}
    return render(request, 'strong/index.html', context=projects)