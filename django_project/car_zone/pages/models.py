from django.db import models

class Team(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.CharField()
    twitter_link = models.CharField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str(self):
        name = f"{self.firstname} {self.lastname}"
        return name