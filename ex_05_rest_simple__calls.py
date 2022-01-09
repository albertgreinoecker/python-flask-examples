import requests

#Einfache Aufrufe des REST-Services

host = 'http://localhost:5000/score'

print('Speichere einen Eintrag am Server:')
response = requests.put('%s/%s' % (host, 'hubert'), data={'score' : 12})
print (response) #Gibt den Response Code aus (Header)
print(response.json()) #Gibt den Response Body aus (also die wirkliche Antwort)

print('---------------------------')
print('Hole diesen Eintrag wieder:')
response = requests.get('%s/%s' % (host, 'hubert')).json()
print (response)

response = requests.patch('%s/%s' % (host, 'hubert'),  data={'score' : 13}).json()
print (response)


print('---------------------------')
print('Löschen :')
response = requests.delete('%s/%s' % (host, 'hubert'))
print (response.status_code)
print (response.json())

response = requests.delete('%s/%s' % (host, 'hubert'))
print (response.status_code)