from django.contrib import admin
from result.models import *
# Register your models here.
@admin.register(marks)
class marks_admin(admin.ModelAdmin):
    list_display = ('marks_ID','student', 'student_name','science','math','computerScience','Total_marks_per_subject','Total_obtained_marks','percentage','passingPercentage','pass_fail')