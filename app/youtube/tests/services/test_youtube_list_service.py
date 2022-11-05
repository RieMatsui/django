from django.utils import timezone
from django.test import TestCase

from youtube.services.youtube_list_service import YoutubeListService


class YoutubeListServiceTests(TestCase):

    def test_get_channels(self):
        youtubeListService = YoutubeListService()
        data = youtubeListService.get_channels()
        print(data)
        self.assertTrue(data)

    def test_get_channel_list(self):
        channel_id = 'UChNkqst-cjAoIbXb-ukn_tQ'
        youtubeListService = YoutubeListService()
        data = youtubeListService.get_channel_list(channel_id)
        print(data)
        self.assertTrue(data)

    def test_get_playlists(self):
        channel_id = 'UChNkqst-cjAoIbXb-ukn_tQ'
        youtubeListService = YoutubeListService()
        data = youtubeListService.get_playlists(channel_id)
        print(data)
        self.assertTrue(data)

