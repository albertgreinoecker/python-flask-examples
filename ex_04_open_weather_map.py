
import requests
import json

import ids


url = 'http://api.openweathermap.org/data/2.5/weather?q=Innsbruck&appid=%s&units=metric' % ids.openweathermap_key

'''
Ein mögliches Ergebnis für obigen Aufruf
{
   "coord":{
      "lon":11.3945,
      "lat":47.2627
   },
   "weather":[
      {
         "id":803,
         "main":"Clouds",
         "description":"broken clouds",
         "icon":"04d"
      }
   ],
   "base":"stations",
   "main":{
      "temp":1.63,
      "feels_like":-0.63,
      "temp_min":-0.4,
      "temp_max":4.52,
      "pressure":1015,
      "humidity":77
   },
   "visibility":10000,
   "wind":{
      "speed":2.06,
      "deg":280
   },
   "clouds":{
      "all":75
   },
   "dt":1641644660,
   "sys":{
      "type":1,
      "id":6872,
      "country":"AT",
      "sunrise":1641625206,
      "sunset":1641656494
   },
   "timezone":3600,
   "id":2775220,
   "name":"Innsbruck",
   "cod":200
}
'''
if __name__ == '__main__':
    response = requests.get(url).json()
    # Formatierte Ausgabe
    print(json.dumps(response, indent=4, sort_keys=False))
    #Schreiben in eine Datei
    with open('/tmp/data.json', 'w') as outfile:
        json.dump(response, outfile)

    #Laden von JSON aus einer Datei
    with open('/tmp/data.json') as json_file:
        data = json.load(json_file)
    print (data)


    # Einfache Abfragen
    longitude = response["coord"]["lon"]
    print (longitude)

    description = response["weather"][0]["description"]
    print(description)


    #Es gibt noch die Methoden
    # * loads: Einlesen von JSON aus einem String (das s steht wie bei dumps für einen String
