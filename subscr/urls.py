from django.urls import path

from subscr.views import UserProfileAPI

urlpatterns = [
    path('bot-users', UserProfileAPI.as_view(), name='bot-users'),
]