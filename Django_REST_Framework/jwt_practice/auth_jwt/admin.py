from django.contrib import admin
from auth_jwt.models import *
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id","user", "role")
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id','role_list')