import requests

# Replace 'YOUR_API_KEY' with your actual API key from Free Currency API
API_KEY = 'fca_live_C5bYvKf17AZ6rQiWB1n5LYFldIh3PuAZ3sWoJF4K'
BASE_URL = 'http://freecurrencyapi.net/api/v1/rates'
CONVERT_URL = 'http://freecurrencyapi.net/api/v1/convert'

def get_exchange_rate(base_currency, target_currency):
    params = {
        'base_currency': base_currency,
        'target_currency': target_currency,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'success' in data and data['success']:
        return data['payload'][target_currency]
    else:
        print("Error occurred:", data['error']['info'])

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

def main():
    print("Welcome to Currency Converter App")
    base_currency = input("Enter the base currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()
    amount = float(input("Enter the amount: "))

    converted_amount = convert_currency(amount, base_currency, target_currency)
    if converted_amount is not None:
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed.")

if __name__ == "__main__":
    main()
