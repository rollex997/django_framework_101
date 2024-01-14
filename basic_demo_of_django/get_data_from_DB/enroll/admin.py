from django.contrib import admin
from enroll.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('SID','name','mobile','email','password')
admin.site.register(Student,StudentAdmin)