import json

from googleapiclient.discovery import build
from rest_framework.views import APIView
from rest_framework.response import Response

from config import settings
from youtube.services.youtube_list_service import YoutubeListService


class YoutubeListApiView(APIView):

    def get(self, request, format=None):
        # YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY
        #
        # youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY, cache_discovery=False)
        #
        # channel_url = "https://www.youtube.com/c/BEFIRSTOfficial"
        # response = youtube.search().list(
        #     part="snippet",
        #     type="channel",  # 検索対象をチャンネルのみに限定
        #     q=channel_url,  # 検索クエリ
        # ).execute()
        # print(response)

        service = YoutubeListService()
        # response = service.get_channel_list()
        #
        # print(json.dumps(response, indent=4, ensure_ascii=False))
        # ダミーデータを返却
        return Response({"name": "DUMMY!"})
