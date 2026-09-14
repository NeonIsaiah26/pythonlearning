import urllib.request, urllib.parse
import http, json, ssl 

serviceurl = 'https://www.openstreetmap.org/#map=6/13.02/121.77'
ctx = ssl.create_default_context()

while True:
    address = input('Enter Location: ')
    if len(address) < 1:
        break
    address = address.strip()
    parms = {}
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'Characters', data[:20].replace('\n'), ' ')

    js = json.loads(data)

    lat = js['features'][0]['properties'][lat]
    lon = js['features'][0]['properties'][lon]
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)
