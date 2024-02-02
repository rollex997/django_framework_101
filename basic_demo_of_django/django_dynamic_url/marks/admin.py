from django.contrib import admin
from  marks.models import *
# Register your models here.
@admin.register(Marks)
class marks_admin(admin.ModelAdmin):
    list_display=(
           'marks_ID', 'Student_ID', 'date_created','date_updated','Maths','Physics', 'Chemistry','Computer','English','Hindi','Total_marks_obtained',
           'Percentage','pass_fail'
    )
@admin.register(MarksSettings)
class marks_settings_admin(admin.ModelAdmin):
    list_display=(
           'marks_settings_ID', 'date_created','date_updated' ,'Total_marks_per_subject', 'passing_percentage','passing_marks_per_subject'
    )