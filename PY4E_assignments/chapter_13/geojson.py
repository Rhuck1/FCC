'''
A simple program that utilizes the json parser to 
demonstrate the parsing of simple a geojson string.
'''

from tempfile import TemporaryFile
import urllib.request, urllib.parse, urllib.error
import json

# Google is increasingly requiring keys for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:

    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)

except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    continue

print(json.dumps(js, indet=4))

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location