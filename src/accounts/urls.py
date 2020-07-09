from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/',views.activate, name='activate'),
]
