from django.db import models
from django.utils import timezone


class MYoutubeChannelModel(models.Model):

    channel_id = models.CharField(primary_key=True, max_length=200, help_text='YoutubeチャンネルのID')
    channel_title = models.CharField(max_length=200, help_text='Youtubeチャンネルタイトル')
    created = models.DateTimeField(help_text='作成日')
    modified = models.DateTimeField(help_text='更新日')
    deleted = models.BooleanField(help_text='削除日')

    def __str__(self):
        return self.channel_title

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.created = timezone.now()  # 新規作成時の時刻を保存
            self.modified = timezone.now()  # 保存されるたびに更新
        return super(MYoutubeChannelModel, self).save(*args, **kwargs)

    class Meta:
        db_table = 'm_youtube_channel_model'

