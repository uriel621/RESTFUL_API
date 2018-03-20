from django.conf.urls import url, include
from strong import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'images', views.image_list)
# router.register(r'images', views.images)

urlpatterns = [
    # url(r'^$', views.strong, name='strong'),
    url(r'^', include(router.urls))
]


