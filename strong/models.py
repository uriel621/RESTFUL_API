from django.db import models

# Create your models here.
# class Project(models.Model):
#     user = models.ForeignKey(User)
#     title = models.CharField(max_length=128)
#     body = models.CharField(max_length=400)

# def get_image_filename(instance, filename):
#     title = instance.post.title
#     slug = slugify(title)
#     return "project_images/%s-%s" % (slug, filename)  



# class Images(models.Model):
#     post = models.ForeignKey(Post, default=None)
#     image = models.ImageField(upload_to=get_image_filename,
#                               verbose_name='Image', )