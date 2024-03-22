import requests

ingredients = input("Please enter the list of ingredients you have, separated by comma: ").lower().split(',')
    
key = '4dd995f78a444a8b8bfba9c8282713d1'

url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={key}&ingredients={",".join(ingredients)}'

api_result = requests.get(url)

api_response = api_result.json()

for recipe in api_response:
    print("Title:", recipe['title'])
    print("Missed Ingredients:")
    for missed_ingredient in recipe['missedIngredients']:
        print("-", missed_ingredient['name'])
    print()