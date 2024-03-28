from django.contrib import admin
from auth_user.models import *
# Register your models here.
@admin.register(UserProfile)
class UserAdminModel(admin.ModelAdmin):
    model = UserProfile
    list_display=('user','role')