from django.contrib import admin
from django.urls import path, include
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path('accounts/', include('accounts.urls')),
]
