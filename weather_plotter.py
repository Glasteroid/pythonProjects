import requests
import numpy as np
from pylab import *

print("Welcome to the weather plotter application!")
user_input = input("Please choose a city you would like to obtain weather data from: ")

params = {
    'api_key': '799b1e124f6928e93849e430a7d2ea25',
    'query': user_input
}

api_result = requests.get('https://api.weatherstack.com/current', params)

api_response = api_result.json()