from django.contrib import admin
from auth_api.models import *
# Register your models here.
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display=('ID','user','phone','created_on')