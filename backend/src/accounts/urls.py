from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts import views
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views


app_name = 'accounts'

urlpatterns = [
    path('signin/token/', views.SignInView.as_view(), name='token_obtain_pair'),
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('email-verify/', views.VerifyEmail.as_view(), name='email-verify')
]
