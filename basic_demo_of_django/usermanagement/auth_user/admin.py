from django.contrib import admin
from auth_user.models import *
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'phone', 'created_on', 'updated_on')