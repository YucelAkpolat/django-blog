from enum import unique
from django.db import models
from autoslug import AutoSlugField


class KategoryModel(models.Model):
    isim = models.CharField(max_length=30,blank=False, null=False)
    slug = AutoSlugField(populate_from='isim',unique=True)


    class Meta:
     db_table= 'Kategori'
     verbose_name_plural = 'Kategoriler'
     verbose_name = 'Kategori'

    def __str__(self):
     return self.isim
 