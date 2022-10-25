import json

from googleapiclient.discovery import build
from rest_framework.response import Response

from config import settings
from youtube.models.m_youtube_channel_model import MYoutubeChannelModel


class YoutubeListApiRepository(Response):

    def __init__(self):
        super().__init__()
        self.api_key = settings.YOUTUBE_API_KEY
        self.version = 'v3'

    def get_channel_by_url(self):
        YOUTUBE_API_KEY = self.api_key

        youtube = build('youtube', self.version, developerKey=YOUTUBE_API_KEY, cache_discovery=False)

        channel_url = "https://www.youtube.com/c/BEFIRSTOfficial"
        response = youtube.search().list(
            part="snippet",
            type="channel",  # 検索対象をチャンネルのみに限定
            q=channel_url,  # 検索クエリ
        ).execute()

        return response

    def get_channels_list(self):
        YOUTUBE_API_KEY = self.api_key

        channel_id = MYoutubeChannelModel.objects.all()[0].channel_id

        youtube = build('youtube', self.version, developerKey=YOUTUBE_API_KEY, cache_discovery=False)

        channel_response = youtube.search().list(
            part='id, snippet',
            channelId=channel_id
        ).execute()

        return channel_response
