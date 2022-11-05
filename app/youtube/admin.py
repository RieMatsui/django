from django.contrib import admin

# Register your models here.

from youtube.models.m_youtube_channel_model import MYoutubeChannelModel

admin.site.register(MYoutubeChannelModel)
