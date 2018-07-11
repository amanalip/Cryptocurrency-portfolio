import os #importing basic libraries
import json
import requests
from datetime import datetime
from prettytable import prettytable
from colorama import Fore, Back, Style

convert = 'USD' #incase the api uses some other currency, depending on the location

listings_url = 'https://api.coinmarket.com/v2/listings/?convert=' + convert #modifying the url

request = requests.get(listings_url) #fetches the data
results = request.json() #converts the data to json format
data = results['data'] #stores the first data of the json tree
ticker_url_pairs = {} #empty dictionary
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url #storing as a key value pair.
