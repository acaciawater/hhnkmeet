'''
Created on Mar 20, 2016

@author: theo
'''

from django.db import models

class MeetProject(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __unicode__(self):
        return self.name
    
