from rest_framework.views import APIView
from rest_framework.response import Response


class YoutubeListApiView(APIView):

    def get(self, request, format=None):
        # ダミーデータを返却
        return Response({"name": "DUMMY!"})