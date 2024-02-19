from django.contrib import admin
from home.models import EmployeeExperience
# Register your models here.
@admin.register(EmployeeExperience)
class EmployeeExperienceAdmin(admin.ModelAdmin):
    list_display = ['ID','company_name','role','date_of_joining','last_date']