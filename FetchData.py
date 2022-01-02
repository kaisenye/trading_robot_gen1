import backtrader as bt
import alpaca_trade_api as tradeapi
from time import sleep 
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import requests, json
import pickle as pkl
import csv
from datetime import date, timedelta

# connecting alpaca_trade_api
api_key='PKLP7X7VL8J4YHAZVCQI'
api_secret='4bTXTMfBMN96g2Of3q6R94ei0bl808OiqW4QEBGn'
alpaca_endpoint = "https://paper-api.alpaca.markets"
api = tradeapi.REST(api_key,api_secret,alpaca_endpoint,api_version='v2')

ORDERS_URL = "https://paper-api.alpaca.markets/v2/orders"
HEADERS = {"APCA-API-KEY-ID":api_key, "APCA-API-SECRET-KEY": api_secret}


# get account status
account = api.get_account()

# Fetch data -----------------------------------------------------------------------------------------------
tickers = []
# tickers and timeframe variables
with open("stocks.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        tickers.append(row)
tickers = [item for sublist in tickers for item in sublist]

# Get time
starting_date = (date.today()-timedelta(days=191)).isoformat()
ending_date = (date.today()-timedelta(days=1)).isoformat()

bars = []
freq = TimeFrame(30, TimeFrameUnit.Minute)
freq = TimeFrame(1, TimeFrameUnit.Day)

bar = api.get_bars(tickers, freq, starting_date, ending_date, adjustment='raw').df
# quotes = api.get_quotes(tickers, starting_date, ending_date, limit=10).df
# trades = api.get_trades(tickers, starting_date, ending_date, limit=10).df

bar.reset_index(inplace = True)
bar.to_pickle('bar.pkl')
# quotes.to_pickle(tickers+'quotes.pkl')
# trades.to_pickle(tickers+'trades.pkl')


