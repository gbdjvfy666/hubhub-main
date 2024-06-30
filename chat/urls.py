# chat/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, GroupChatViewSet, UserViewSet, ProfileViewSet, ProfileUpdateView, UserListView, chat_index

router = DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'groupchats', GroupChatViewSet)
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', chat_index, name='chat-index'),
    path('', include(router.urls)),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('users/list/', UserListView.as_view(), name='user-list'),
]
