from django.contrib import admin
from viewSet.models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['ID','name','roll','city']