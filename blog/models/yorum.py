from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

from blog.models.yazi import YazilarModel


class YorumModel(models.Model):
    yazan = models.ForeignKey(User,on_delete=models.CASCADE,related_name='yorum')
    yazı =  models.ForeignKey(YazilarModel, on_delete=models.CASCADE,related_name='yorumlar')
    yorum = models.TextField()
    olusturulma_tarihi= models.DateField(auto_now_add=True)
    guncellenme_tarihi =models.DateField(auto_now=True)


    class Meta:
        db_table='yorum'
        verbose_name ='Yorum'
        verbose_name_plural='Yorumlar'
    def __str__(self):
        return self.yorum
    
