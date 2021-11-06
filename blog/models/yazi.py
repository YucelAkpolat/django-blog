from django.db import models

from django.db.models.deletion import CASCADE
from blog.models import KategoryModel
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class YazilarModel(models.Model):
    resim =models.ImageField(upload_to='yazılar_resim')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    olusturulma_tarih = models.DateField(auto_now_add=True)
    duzenlenme_tarihi = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from='baslik',unique=True)
    kategoriler = models.ManyToManyField(KategoryModel,related_name='yazi')
    yazar = models.ForeignKey(User,on_delete=models.CASCADE,related_name='yazilar')


    class Meta:
       verbose_name = 'Yazi'
       verbose_name_plural= 'Yazilar'
       db_table= 'Yazi'
  

    def __str__(self):
        return self.baslik
    
       
