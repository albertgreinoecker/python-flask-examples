
import requests
import json
import ids

url = 'http://api.openweathermap.org/data/2.5/weather?q=Innsbruck&appid=%s&units=metric' % ids.openweathermap_key



if __name__ == '__main__':
    response = requests.get(url).json()
    print (response)