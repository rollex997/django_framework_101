from django.contrib import admin
from task1.models import *

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'email', 'category_list')  # Include category_list in list_display

    def category_list(self, obj):
        return ', '.join([cat.category for cat in obj.category.all()])

    category_list.short_description = 'category'

@admin.register(StudentCategory)
class StudentCategoryAdmin(admin.ModelAdmin):
    list_display=('id','category')
    list_display_links=('category',)