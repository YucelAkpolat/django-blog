from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CostomUserModel

from account.models import CostomUserModel

# Register your models here.
class CostomAdmin(UserAdmin):
    model = CostomUserModel
    list_display =('username','email')
    fieldsets = UserAdmin.fieldsets + (
            ("Avatar Değiştirme Alanı", {
                'fields':  ['avatar']
            }),
                
    )
       
    

admin.site.register(CostomUserModel,CostomAdmin)