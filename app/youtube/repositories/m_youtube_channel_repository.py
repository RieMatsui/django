from youtube.models.m_youtube_channel_model import MYoutubeChannelModel


class MYoutubeChannelRepository:

    def get_all(self):
        m_channel = MYoutubeChannelModel()
        return m_channel.objects.all()
