# simple weather app

import requests
import json
import datetime as dt

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = open('api_key.txt', 'r').read().strip()  # Added strip() to remove leading/trailing whitespaces
CITY = "Kenya"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# Using requests.get with parameters
params = {
    'q': CITY,
    'appid': API_KEY
}
response = requests.get(BASE_URL, params=params).json()

# Use json.dumps to format the JSON response with indentation
formatted_response = json.dumps(response, indent=2)


temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
wind_speed = response['wind']['speed']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f} celsius or {temp_fahrenheit} fahrenheit")
print(f"The wind in the {CITY} is: {description}")
print(f"sunrise is at {sunrise_time} local time")


#print(formatted_response)

