import pandas as pd

from googleapiclient.discovery import build
from rest_framework.response import Response

from config import settings

class YoutubeListApiRepository(Response):

    def __init__(self):
        super().__init__()
        self.api_key = settings.YOUTUBE_API_KEY
        self.version = 'v3'
        self.service_name = 'youtube'
        self.api_setting = build(self.service_name, self.version, developerKey=self.api_key)

    def get_channel_by_url(self):
        youtube = self.api_setting
        channel_url = "https://www.youtube.com/c/BEFIRSTOfficial"
        response = youtube.search().list(
            part="snippet",
            type="channel",  # 検索対象をチャンネルのみに限定
            q=channel_url,  # 検索クエリ
        ).execute()

        return response

    def get_channels_list(self, channel_id):
        channels = []  # チャンネル情報を格納する配列
        searches = []  # videoidを格納する配列
        videos = []  # 各動画情報を格納する配列
        next_page_token = None
        token = None
        youtube = self.api_setting

        channel_response = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        ).execute()

        for channel_result in channel_response.get("items", []):
            if channel_result["kind"] == "youtube#channel":
                channels.append([channel_result["snippet"]["title"], channel_result["statistics"]["subscriberCount"],
                                 channel_result["statistics"]["videoCount"], channel_result["snippet"]["publishedAt"]])

        while True:
            if next_page_token is not None:
                token = next_page_token

            search_response = youtube.search().list(
                part="snippet",
                channelId=channel_id,
                maxResults=50,
                order="viewCount",
                pageToken=token
            ).execute()

            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    searches.append(search_result["id"]["videoId"])

            try:
                next_page_token = search_response["nextPageToken"]
            except:
                break

        for result in searches:
            video_response = youtube.videos().list(
                part='snippet, statistics',
                id=result
            ).execute()

            for video_result in video_response.get("items", []):
                if video_result["kind"] == "youtube#video":

                    videos.append([video_result["snippet"]["title"], video_result["statistics"]["viewCount"],
                                   video_result["statistics"]["likeCount"],
                                   video_result["statistics"]["commentCount"], video_result["snippet"]["publishedAt"]])

        videos_report = pd.DataFrame(videos, columns=['title', 'viewCount', 'likeCount', 'commentCount',
                                                      'publishedAt'])
        videos_report.to_csv(settings.APP_URL + "youtube/static/data/videos_report.csv")

        channel_report = pd.DataFrame(channels, columns=['title', 'subscriberCount', 'videoCount', 'publishedAt'])
        channel_report.to_csv(settings.APP_URL + "youtube/static/data/channels_report.csv")

        return channel_response

    def get_playlists(self, channel_id):

        playlists = []
        playlist_items = []
        videos = []
        youtube = self.api_setting

        playlists_results = youtube.playlists().list(
            part='snippet',
            channelId=channel_id,
            maxResults=50
        ).execute()

        for playlists_result in playlists_results.get("items", []):

            print(playlists_result)
            playlists.append([playlists_result['id'], playlists_result['snippet']['title']])

            playlist_items_list_request = youtube.playlistItems().list(
                playlistId=playlists_result['id'],
                part="snippet",
                maxResults=50
            ).execute()

            for playlist_item_result in playlist_items_list_request.get("items", []):

                title = playlist_item_result["snippet"]["title"]
                video_id = playlist_item_result["snippet"]["resourceId"]["videoId"]
                playlist_items.append([video_id, title])

                video_response = youtube.videos().list(
                    part='snippet, statistics',
                    id=video_id
                ).execute()

                print(video_response)

                for video_result in video_response.get("items", []):
                    if video_result["kind"] == "youtube#video":

                        statistics = video_result.get('statistics', [])
                        snippet = video_result.get('snippet', [])

                        videos.append([video_id,
                                       snippet.get("title", ''),
                                       statistics.get("viewCount", 0),
                                       statistics.get("likeCount", 0),
                                       statistics.get("commentCount", 0),
                                       snippet.get("publishedAt", ''),
                                       ])

        playlists_report = pd.DataFrame(playlists, columns=['etag', 'id'])
        playlists_report.to_csv(settings.APP_URL + "youtube/static/data/playlists_report.csv")

        playlist_items_report = pd.DataFrame(playlist_items, columns=['video_id', 'title'])
        playlist_items_report.to_csv(settings.APP_URL + "youtube/static/data/playlist_itmes_report.csv")

        playlists_video_report = pd.DataFrame(videos, columns=['video_id', 'title', 'view_count', 'like_count', 'comment_count',
                                                      'publishedAt'])
        playlists_video_report.to_csv(settings.APP_URL + "youtube/static/data/playlists_video_report.csv")

        return playlist_items










