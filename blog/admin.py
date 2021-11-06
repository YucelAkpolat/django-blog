from django.contrib import admin
from blog.models import KategoryModel
from blog.models import YazilarModel
from blog.models import YorumModel
from blog.models import IletisimModel

# Register your models here.


admin.site.register(KategoryModel)


class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik')
    list_display=(
        'baslik','olusturulma_tarih','duzenlenme_tarihi'
    )

admin.site.register(YazilarModel, YazilarAdmin)

class YorumAdmin(admin.ModelAdmin):
    search_fields=('yazan__username',)

    list_display=(
        'yazan','olusturulma_tarihi','guncellenme_tarihi'
    )
admin.site.register(YorumModel,YorumAdmin)



class IletisimAdmin(admin.ModelAdmin):
    search_fields=('email',)

    list_display=(
        'email','olusturulma_tarihi',
    )
admin.site.register(IletisimModel,IletisimAdmin)