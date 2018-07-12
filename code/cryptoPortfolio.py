import os #importing basic libraries
import json
import requests#You need to install using pip
from datetime import datetime
from prettytable import prettytable#You need to install using pip
from colorama import Fore, Back, Style#You need to install using pip

convert = 'USD' #incase the api uses some other currency, depending on the location

listings_url = 'https://api.coinmarket.com/v2/listings/?convert=' + convert #modifying the url
url_end = '?structure=array&convert=' + convert #convert everything to USD
request = requests.get(listings_url) #fetches the data
results = request.json() #converts the data to json format
data = results['data'] #stores the first data of the json tree
ticker_url_pairs = {} #empty dictionary
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url #storing as a key value pair.

print()
print("My Portfolio")
print()

portfolio_value = 0.00 #initialising the values
last_updated = 0
#creating the table
table = Prettytable(['Asset', 'Amount Owned', convert + 'Value', 'Price', '1h', '24h', '7d'])

with open("portfolio.txt") as inp: #sends the file as input
    for line in inp: #for each line in a file
        ticker,amount = line.split() #split the line at a space bar
        ticker = ticker.upper() #incase the data is in small
        #url+ID of the cryptocurrency + atructure in which we want the data (array/dictionary)+convert to standard USD
        ticker_url = 'https://api.coinmarket.com/v2/ticker/' + str(ticker_url_pairs[ticker]) + '/' + url_end
