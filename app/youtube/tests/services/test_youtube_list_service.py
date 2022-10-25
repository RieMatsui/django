from django.utils import timezone
from django.test import TestCase

from youtube.models.m_youtube_channel_model import MYoutubeChannelModel
from youtube.services.youtube_list_service import YoutubeListService


class YoutubeListServiceTests(TestCase):

    def test_get_channels(self):
        youtubeListService = YoutubeListService()
        data = youtubeListService.get_channels()

        self.assertTrue(data)

    def test_get_channel_list(self):

        youtubeListService = YoutubeListService()
        data = youtubeListService.get_channel_list()
        print(data)
