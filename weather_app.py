import requests
import json

# access key allows user to access API
access_key = '799b1e124f6928e93849e430a7d2ea25'

# choose location
location = input("What city would you like to know about? ")

api_result = requests.get(f'http://api.weatherstack.com/current?access_key={access_key}&query={location}')

api_response = api_result.json()

string_api_response = str(api_response).replace("'", '"')

json_dict = json.loads(string_api_response)

str1 = '\n'

print(str1.join(list(json_dict['current'].keys())))
user_input = input(f"Which of these would you like to know about {location} currently? ").lower()

print(f'Location {user_input} is ' + str(json_dict['current'][user_input]))