from youtube.repositories.m_youtube_channel_repository import MYoutubeChannelRepository
from youtube.repositories.youtube_list_api_repository import YoutubeListApiRepository


class YoutubeListService(object):

    def __init__(self):
        self.m_channel = MYoutubeChannelRepository()
        self.youtube_list_api = YoutubeListApiRepository()

    def get_all(self):
        channels = self.m_channel.get_all()
        return channels

    def get_channels(self):
        channels = self.youtube_list_api.get_channel_by_url()
        return channels

    def get_channel_list(self, channel_id):
        channel_list = self.youtube_list_api.get_channels_list(channel_id)
        return channel_list

    def get_playlists(self, channel_id):
        playlists = self.youtube_list_api.get_playlists(channel_id)
        return playlists



