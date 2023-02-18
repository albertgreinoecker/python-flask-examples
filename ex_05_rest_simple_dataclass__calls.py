import requests

host = 'http://localhost:5000/person'

print('Speichere einen Eintrag am Server:')
response = requests.put('%s/%d' % (host, 3), json={'id' : 3, 'name' : 'Franz', 'age' : 50, 'comment' : 'neu'})
print (response) #Gibt den Response Code aus (Header)
print(response.json()) #Gibt den Response Body aus (also die wirkliche Antwort)

print('---------------------------')
print('Hole diesen Eintrag wieder:')
response = requests.get('%s/%d' % (host, 3)).json()
print (response)

response = requests.patch('%s/%s' % (host, 3),  json={'age' : 12}).json()
print (response)

print('---------------------------')
print('Hole diesen Eintrag wieder:')
response = requests.get('%s/%d' % (host, 3)).json()
print (response)

# print('---------------------------')
# print('Löschen :')
# response = requests.delete('%s/%s' % (host, 3))
# print (response.status_code)
# print (response.json())
