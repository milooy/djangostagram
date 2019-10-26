from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('dsuser.Dsuser', on_delete=models.CASCADE, verbose_name='작성자')
    image_url = models.CharField(max_length=500, verbose_name='이미지 주소')
    text = models.TextField(max_length=500, verbose_name='내용')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='작성일')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
