from django.contrib import admin
from student.models import *
# Register your models here.
@admin.register(Student_info)
class StudentInfo_Admin(admin.ModelAdmin):
    list_display = ('student_ID','name','roll_no','mobile','father_name','mother_name','father_mobile')