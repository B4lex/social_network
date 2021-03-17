# from django.urls import path, reverse_lazy
# from django.contrib.auth import views as auth_views
#
# from accounts import views
#
#
# app_name = 'accounts'
#
# urlpatterns = [
#     path('login/', views.UserLoginView.as_view(), name='login'),
#     path('register/', views.UserRegisterView.as_view(), name='register'),
#     path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
#     path('edit_profile/', views.UserEditView.as_view(), name='profile-edit'),
#     path('password_change/', auth_views.PasswordChangeView.as_view(
#              template_name='auth/password_change.html',
#              success_url=reverse_lazy('accounts:password-change-done')
#          ),
#          name='password-change'),
#     path('password_change_done/',
#          auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'),
#          name='password-change-done'),
#     path('people/', views.UserListView.as_view(), name='people-list'),
#     path('people/<slug:username>', views.UserDetailView.as_view(), name='person-detail'),
#     path('follow/', views.follow_person)
# ]
