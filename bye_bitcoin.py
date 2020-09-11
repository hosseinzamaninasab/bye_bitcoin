import requests


def let_know_name():
    print("ASAP Buy Bitcoin")


my_price = 11000

response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(response.json()['data']['amount'])
# print("At this moment, Bitcoin is %i Dollars" % price)
if price <= my_price:
    let_know_name()
