from django.db import models

# Create your models here.
class Project(models.Model):
    type_of_project = models.CharField(max_length=200)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.type_of_project

def get_image_filename(instance, filename):
    return "strong/{}/{}".format(instance.project, filename)  

def name_of_project(name):
    new_name = ''
    counter = 0
    for letter in str(name):
        if letter == '/':
            counter += 1
            if counter == 2:
                break
        else:
            new_name += letter
    new_name = new_name.replace('strong', '')
    return "{} Images".format(new_name) 

class Images(models.Model):  
    project = models.ForeignKey(Project, related_name="images")
    image = models.ImageField(upload_to=get_image_filename)
    def __str__(self):
        return name_of_project(self.image)
    