import requests

#Einfache Aufrufe von REST-Services anhand eines Testervers

host = 'https://jsonplaceholder.typicode.com'

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
j = response.json()

print(response.text)
print(response.status_code)
print(response.headers)
print(response.headers['content-type'])
print(j)


response = requests.options('https://jsonplaceholder.typicode.com/todos/1')
print(response.headers['Access-Control-Allow-Methods'])

print("--------------------------------")

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

print("------DELETE:")
response = requests.delete('https://jsonplaceholder.typicode.com/todos/1')
print(response.status_code)

print("------HEAD:")
response = requests.head('https://jsonplaceholder.typicode.com/todos/1', timeout=1)
print(response.headers)