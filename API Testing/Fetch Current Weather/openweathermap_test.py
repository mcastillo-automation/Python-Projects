"""
Simple script to check for weather based on user ip.
Uses geocoder and the openweathermap api to accomplish this.
"""
from geocoder import ip
import requests
import config

API_KEY = config.API_KEY
ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

g = ip("me")
lat = g.lat
lon = g.lng

weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': API_KEY,
    'units': 'imperial'
}

response_weather = requests.get(ENDPOINT, params=weather_params, timeout=5)

response_weather.raise_for_status()

weather_json = response_weather.json()

weather_condition = weather_json["weather"][0]["main"].lower()
sky_condition = weather_json["weather"][0]["description"]
current_temp = weather_json["main"]["temp"]
feels_like = weather_json["main"]["feels_like"]
temp_max = weather_json["main"]["temp_max"]
temp_min = weather_json["main"]["temp_min"]

print(
    f"Today's weather will be {weather_condition} with a\
 {sky_condition}.\n"
    f"Current temperature is {current_temp} degrees fahrenheit\
 but it feels like {feels_like} fahrenheit.\n"
    f"Today's max is {temp_max} fahrenheit\
 with a min of {temp_min} fahrenheit."
)
