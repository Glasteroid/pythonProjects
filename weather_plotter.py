import requests
import numpy as np
from pylab import *

print("Welcome to the weather plotter application!")
user_city = input("Please choose a city you would like to obtain weather data from: ")
user_date = input("Please choose a date in the city you chose you would like to obtain the hourly weather forecast from in the form (Year-Month-Day): ")

params = {
    'access_key': '799b1e124f6928e93849e430a7d2ea25',
    'query': user_city,
    'historical_date': user_date
}

api_result = requests.get('http://api.weatherstack.com/historical', params)

api_response = api_result.json()

print(api_response)