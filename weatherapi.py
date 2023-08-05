
import requests
import json

city = input('Enter the name of the city: ')
api_key = "8c0809cde427e89becc66d052ad2a05b"  
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
json_data = requests.get(api).json()

if json_data['cod'] == 200:
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    print('Weather in', city)
    print('The temperature is:', temp, '°C')
    print('Pressure is:', pressure, 'hPa')
    print('Humidity is:', humidity, '%')
    print('Wind speed is:', wind, 'm/s')
else:
    print('City not found or error in retrieving data. Please check the city name or try again later.')
