from django.contrib import admin
from marks.models import *
# Register your models here.
@admin.register(Marks)
class MarksModelAdmin(admin.ModelAdmin):
    list_display = ('id','student','maths','physics','chemistry','english','hindi')
    list_display_links = ('id','student',)