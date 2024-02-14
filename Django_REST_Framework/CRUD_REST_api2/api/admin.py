from django.contrib import admin
from api.models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Student_ID','name','roll','city')