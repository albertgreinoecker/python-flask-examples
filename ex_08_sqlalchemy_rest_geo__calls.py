import requests


response = requests.put('http://localhost:5000/geoinfo/0' , data={'info' : {'name' : 'albert', 'long' : 1, 'lat' : 2} })
print(response)
print(response.json())


response = requests.get('http://localhost:5000/geoinfos')
print(response)
print(response.json())