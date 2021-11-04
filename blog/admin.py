from django.contrib import admin
from blog.models import KategoryModel
from blog.models import YazilarModel

# Register your models here.


admin.site.register(KategoryModel)


class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik')
    list_display=(
        'baslik','olusturulma_tarih','duzenlenme_tarihi'
    )

admin.site.register(YazilarModel, YazilarAdmin)