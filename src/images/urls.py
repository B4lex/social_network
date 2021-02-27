from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.list_images, name='list_images'),
    path('create/', views.image_create, name='image_create')
]