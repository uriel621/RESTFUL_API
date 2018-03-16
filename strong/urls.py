from django.conf.urls import url
from strong import views

urlpatterns = [
    url(r'^$', views.strong, name='strong')
]

    # url(r'^$', views.index, name='index'),
    # url(r'^form/', views.form_view, name='form_view'),