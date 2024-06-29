from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    AnnouncementListView, AnnouncementDetailView, AnnouncementCreateView, 
    AnnouncementUpdateView, ResponseCreateView,
    ResponseDeleteView,
    response_list, delete_response, accept_response
)
from main import views

urlpatterns = [
    path('announcement/<int:announcement_id>/create-response/', ResponseCreateView.as_view(), name='create-response'),
    path('announcement/<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('', AnnouncementListView.as_view(), name='announcement-list'),
    path('announcements/', views.AnnouncementListView.as_view(), name='announcement_list'),
    path('announcement/create/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('announcement/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('response/<int:pk>/delete/', ResponseDeleteView.as_view(), name='response-delete'),
    path('responses/', response_list, name='response-list'),
    path('responses/delete/<int:announcement_id>/', delete_response, name='delete-response'),
    path('responses/accept/<int:announcement_id>/', accept_response, name='accept-response'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

