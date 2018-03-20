from django.shortcuts import render
from strong.models import Project, Images
from django.conf import settings

from rest_framework import viewsets
from strong.serializers import ProjectSerializers#, ImagesSerializers

# settings.MEDIA_URL = '/media/' 

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def strong(request):
#     project_model = Project.objects.order_by('type_of_project')
#     images_model = Images.objects.order_by('image')
#     projects = {'project_model':project_model, 'images_model':images_model}
#     # settings.MEDIA_URL = '/strong/images/' # dosent work FIX IT
#     return render(request, 'strong/index.html', context=projects)

class image_list(viewsets.ModelViewSet):
    queryset = Project.objects.all()  
    serializer_class = ProjectSerializers