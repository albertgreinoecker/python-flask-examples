import os
import requests


with open('./test_files/htl-logo.png', 'rb') as f:
    data = f.read()

response = requests.put('http://localhost:5000/file/xy.png' ,data=data)
print(response)
print(response.json())

# response = requests.delete('http://localhost:5000/file/xx.png')
# print(response)
# print(response.json())

# response = requests.get('http://localhost:5000/file/xx.png')
# print(response)
# with open(os.path.join('/tmp/result.png'), "wb") as fp:
#     fp.write(response.content)


response = requests.get('http://localhost:5000/files/')
print(response)
print(response.json())