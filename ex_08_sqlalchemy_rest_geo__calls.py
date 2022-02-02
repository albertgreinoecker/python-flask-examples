import json

import requests

j = {'name' : 'albert', 'long' : 11.400375, 'lat' : 47.259659, 'message' : 'test'}
print(j)
response = requests.put('https://os-beyond.at/htl/geo/geoinfo/0' , json={'info' : j})
#response = requests.put('http://localhost:5000/geoinfo/0' , json={'info' : j})
print(response)
print(response.json())



#response = requests.get('https://os-beyond.at/htl/geo/geoinfos')
# response = requests.get('http://localhost:5000/geoinfos')
# print(response)
# print(response.json())

# response = requests.delete('http://localhost:5000/geoinfo/4')
# print(response)
# print(response.json())


# j = json.dumps({'message' : 'modified message'})
# response = requests.patch('http://localhost:5000/geoinfo/5' , data={'info' : j})
# print(response)
# print(response.json())