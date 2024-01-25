from django.contrib import admin

# Register your models here.
from student.models import *
@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    list_display = ('student_ID', 'student_name', 'roll_no','mobile','father_name','mother_name','father_mobile')