from django.urls import path, include
from rest_framework import routers
from images.views import ImageViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('event', ImageViewSet)
urlpatterns = [

    path('', include(router.urls)),

]