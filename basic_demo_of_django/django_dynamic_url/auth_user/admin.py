from django.contrib import admin
from auth_user.models import *
# Register your models here.
@admin.register(User_profile)
class User_profileAdmin(admin.ModelAdmin):
    list_display = ('user','userRole',) 