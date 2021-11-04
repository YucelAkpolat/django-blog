from django.db import models
from autoslug import AutoSlugField
from django.db.models.deletion import CASCADE
from blog.models import KategoryModel
from django.contrib.auth.models import User


class YazilarModel(models.Model):
    resim =models.ImageField(upload_to='yazılar_resim')
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    olusturulma_tarih = models.DateField(auto_now_add=True)
    duzenlenme_tarihi = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from='baslik',unique=True)
    kategoriler = models.ManyToManyField(KategoryModel,related_name='yazi')
    yazar = models.ForeignKey(User,on_delete=CASCADE,related_name='yazilar')


    class Meta:
       verbose_name = 'Yazi'
       verbose_name_plural= 'Yazilar'
    def __str__(self):
        return self.baslik
    
       
