from django.db import models

class groups(models.Model):
    group_id = models.IntegerField(max_length=30)
    
    def __unicode__(self):
        return self.group_id

