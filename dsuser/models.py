from django.conf import settings
from django.db import models
from django.utils import timezone


class Dsuser(models.Model):
    username = models.CharField(max_length=128, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password = models.CharField(max_length=100, verbose_name='비밀번호')
    registered_datetime = models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'ds_user'
        verbose_name = '장고스타그램 사용자'
        verbose_name_plural = '장고스타그램 사용자'
