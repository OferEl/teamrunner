from django.db import models
from django.contrib.auth.models import User


class user(models.Model):
    user_id = models.IntegerField(max_length=30)
    user_name = models.CharField(max_length=50)
    user_lastname = models.CharField(max_length=60)
    user_city = models.CharField(max_length=50)
    user_status = models.CharField(max_length=1)
    user_email = models.EmailField()
    gender = models.CharField(max_length=1)
    password = models.CharField(max_length=50)
    password_date = models.DateField()
    create_date = models.DateField()
    
    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    city   = models.CharField(max_length=50)
    age    = models.IntegerField(max_length=2)
    gender = models.IntegerField(max_length=1)