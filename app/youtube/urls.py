from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from youtube.views.youtube_search import YoutubeListApiView

router = DefaultRouter()

urlpatterns = [
    path('dummy/', YoutubeListApiView.as_view()),
]

