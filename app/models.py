from distutils.command.upload import upload
from turtle import up
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  title = models.CharField("タイトル",max_length=200)
  image = models.ImageField(upload_to='images', verbose_name='イメージ画像',null=True,blank=True)
  content = models.TextField("本文")
  created = models.DateTimeField("作成日",default=timezone.now)

  def __str__(self):
    return self.title