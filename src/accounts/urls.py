from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.test_view, name='register'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard')
]
