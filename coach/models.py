from django.db import models

class coach(models.Model):
    coach_id = models.IntegerField(max_length=30)
    coach_name = models.CharField(max_length=50)
    coach_lastname = models.CharField(max_length=60)
    coach_area = models.CharField(max_length=30)
    coach_city = models.CharField(max_length=50)
    coach_status = models.CharField(max_length=1)
    create_date = models.DateField()
    
    def __unicode__(self):
        return self.name

