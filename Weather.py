import requests
import os

user_api = os.environ['weatherReportApi']
location ="Nagpur"

complete_api = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
api_link = requests.get(complete_api)
api_data = api_link.json()

temp_city =(api_data['main']['temp']) - 273
weather_desc = api_data['weather'][0]['description']

