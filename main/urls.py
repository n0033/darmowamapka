from django.urls import path
from .views import (
    MainView,
    clip,
    video_watched,
    ebook_sent,
)

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('clip/', clip, name='clip'),
    path('ebook_sent/', ebook_sent, name='send'),
    path('video_watched/', video_watched),
]
