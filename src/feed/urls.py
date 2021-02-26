from django.urls import path
from feed import views

app_name = 'feed'

urlpatterns = [
    path('dashboard/', views.FeedView.as_view())
]
