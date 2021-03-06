from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.list_images, name='list_images'),
    path('create/', views.image_create, name='image_create'),
    path('update/<int:pk>', views.images_update, name='images_update'),
    path('delete/<int:pk>', views.image_delete, name='image_delete'),
    path('detail/<int:pk>/<slug:slug>', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
]