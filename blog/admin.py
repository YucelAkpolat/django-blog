from django.contrib import admin
from blog.models import KategoryModel
from blog.models import YazilarModel

# Register your models here.


admin.site.register(KategoryModel)


admin.site.register(YazilarModel)