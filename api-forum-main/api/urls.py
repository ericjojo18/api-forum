from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets.subject_viewset import SubjectViewSet
from .viewsets.forum_viewset import ForumViewSet
from .viewsets.message_viewset import MessageViewSet


router = routers.DefaultRouter()
router.register(r'forum', ForumViewSet, basename='forum')
router.register(r'subject', SubjectViewSet, basename='sujet')
router.register(r'message', MessageViewSet, basename='message')


app_name = 'api'

urlpatterns = [ 
    path('', include(router.urls))
]