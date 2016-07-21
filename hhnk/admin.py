'''
Created on Mar 21, 2016

@author: theo
'''
from django.contrib import admin
from hhnk.models import MeetProject

@admin.register(MeetProject)
class MeetAdmin(admin.ModelAdmin):
    pass
