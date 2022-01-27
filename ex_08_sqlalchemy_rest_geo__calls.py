import json

import requests

j = json.dumps({'name' : 'albert', 'long' : 1, 'lat' : 2, 'message' : 'test'})
print(j)
response = requests.put('http://localhost:5000/geoinfo/0' , data={'info' : j})
print(response)
print(response.json())


response = requests.get('http://localhost:5000/geoinfos')
print(response)
print(response.json())