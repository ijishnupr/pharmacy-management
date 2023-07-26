from django.contrib import admin
from .models import medicine

@admin.register(medicine)
class medicineAdmin(admin.ModelAdmin):
    list_display=('id','title','price','status','exp')
