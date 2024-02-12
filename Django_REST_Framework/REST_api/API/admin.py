from django.contrib import admin
from API.models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('Student_ID','name','roll','city','created_at','updated_at')