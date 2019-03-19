print("hello, world")
import urllib.request
import json

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
city = 'Wellesley'
country_code = 'us'
url = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'.format(
    city=city, country_code=country_code, APIKEY=APIKEY)

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)

# How do we get current temperature?
weather='coord': {'lon': -71.29, 'lat': 42.3}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 277.23, 'pressure': 1028, 'humidity': 35, 'temp_min': 275.93, 'temp_max': 278.15}, 'visibility': 16093, 'wind': {'speed': 5.7, 'deg': 290}, 'clouds': {'all': 75}, 'dt': 1553011422, 'sys': {'type': 1, 'id': 5255, 'message': 0.0086, 'country': 'US', 'sunrise': 1552992638, 'sunset': 1553036120}, 'id': 4954738, 'name': 'Wellesley', 'cod': 200}

import pprint

pprint.pprint(weather
)
print(weather{"main"}{"temp"}-273.15)
