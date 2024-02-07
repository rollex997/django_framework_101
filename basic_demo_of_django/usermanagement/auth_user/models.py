from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles',null=True)
    phone = models.BigIntegerField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)