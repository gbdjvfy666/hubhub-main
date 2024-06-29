from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import register,logout_view
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', logout_view, name='logout'),
]