'''
Created on Jul 2, 2016

@author: theo
'''
from django.http import JsonResponse
from .models import MeetProject
from iom.views import ContextMixin
from django.views.generic import TemplateView
from django.core import serializers

import requests, json
from httplib import HTTPResponse

def get_json(request,path=None):
    ''' forward request to all projects '''
    result = {}
    path = path or request.get_full_path()
    for p in MeetProject.objects.all():
        url = p.url + path
        response = requests.get(url)
        result[p.url] = response.text 
    return HTTPResponse(result, content_type='application/json')

def get_objects(request,path=None):
    ''' forward request to all projects '''
    objects = []
    path = path or request.get_full_path()
    for p in MeetProject.objects.all():
        url = p.url + path
        response = requests.get(url)
        objects.extend(serializers.deserialize('json', response.text))
    return objects

def get_waarnemers(request):
    return get_json(request,'/get/waarnemers')

def get_meetpunten(request):
    return get_json(request,'/get/meetpunten')

def get_waarnemingen(request):
    return get_json(request,'/get/waarnemingen')

class HomeView(ContextMixin,TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if self.request:
            waarnemers = [o.object for o in get_objects(self.request, '/get/waarnemers')]
            context['waarnemers'] = waarnemers 
        context['maptype'] = 'ROADMAP'
        return context
