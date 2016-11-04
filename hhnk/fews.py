'''
Created on Nov 1, 2016

@author: theo
'''
import requests
from urllib import urlencode
import datetime, time

def timestamp(dt=datetime.datetime.utcnow()):
    return int(time.mktime(dt.utctimetuple())*1000)

if __name__ == '__main__':
#    url = 'https://api.ddsc.nl/api/v2/timeseries/?format=json&location__organisation__name=HHNK&name__in=(CL,EGVms_cm.meting)'
#    url = 'https://api.ddsc.nl/api/v2/timeseries/?format=json&location__organisation__name=HHNK&name__startswith=EGV'
    headers = {'username': 'acacia', 'password': '123Acacia321'}
    names = {}
    url = 'https://api.ddsc.nl/api/v2/timeseries/?'
    start = timestamp(datetime.datetime(2015,1,1))
    end = timestamp(datetime.datetime.utcnow())
    params = {'format':'json',
              'location__organisation__name':'HHNK',
              'name__startswith':'EGV',
              'start':start,
              'end':end}
    params = urlencode(params)
    url = url + params
    while url:
        print url
        response = requests.get(url = url, headers = headers)
        resp = response.json()
        url = resp['next']
        for p in resp['results']:
            name = p['name']
            disp = '-'
            unit = '-'
            try:
                disp = p['observation_type']['parameter_short_display_name']
                unit = p['observation_type']['referenced_unit_short_display_name']
                events= p['events']
            except:
                pass
            print name, disp, unit, len(events)
            if not name in names:
                names[name] = (disp,unit,len(events))
    for k,v in names.items():
        print k,v
        