from django.contrib import admin
from testapp.models import Employ

# Register your models here.
class EmployAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eadress']
    
admin.site.register(Employ,EmployAdmin)    