from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    city   = models.CharField(max_length=50)
    age    = models.IntegerField(max_length=2)
    gender = models.IntegerField(max_length=1)
    

#coach- coachid, coach_name, coach_lastname, coach_area, coach_city,status

#class coach (models.Model):
    coachid= models.IntegerField(max_length=11,null= False)
    coach_name=models.CharField(max_length=50,null= False)
    coach_lastname=models.CharField(max_length=50,null= False)
    #coach_area=
    #coach_city=
    coach_pic= models.ImageField(storage=fs,null= True)
    coach_status= models.IntegerField(max_length=1,null= False)    
    coach_email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    coach_comments = models.CharField(max_length=500,null= True)
    