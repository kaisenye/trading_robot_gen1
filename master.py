def porfolio_status(api):
    # Get account info
    account = api.get_account()

    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print ('Account is currently restricted from trading.')
    else:
        print ("Accouont status is", account.status)

    # Check how much money we can use to open new positions.
    print('Available buying power ${}.'.format(account.buying_power))
    # Check our current balance vs. our balance at the last market close
    balance_change = float(account.equity) - float(account.last_equity)
    print(f'Today\'s portfolio balance change: ${balance_change}')

    # Get a list of all of our positions.
    portfolio = api.list_positions()
    # Print the quantity of shares for each position.
    for position in portfolio:
        print("{}: {} shares".format(position.symbol, position.qty))
  
def market_time(api, date = '2018-12-01'):
    # Check if the market is open now.
    clock = api.get_clock()
    print('The market is {}'.format('open.' if clock.is_open else 'closed.'))
    # Check when the market was open on Dec. 1, 2018
    calendar = api.get_calendar(start=date, end=date)[0]
    print('The market opened at {} and closed at {} on {}.'.format(
        calendar.open,
        calendar.close,
        date
    ))

import backtrader as bt
import alpaca_trade_api as tradeapi
from time import sleep 
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import requests, json
import pickle as pkl
import csv
from datetime import date, timedelta
from local_settings import alpaca_paper

# connecting alpaca_trade_api
api_key = alpaca_paper['api_key']
api_secret = alpaca_paper['api_secret']
alpaca_endpoint = alpaca_paper['alpaca_paper']

api = tradeapi.REST(api_key,api_secret,alpaca_endpoint,api_version='v2')

ORDERS_URL = "https://paper-api.alpaca.markets/v2/orders"
HEADERS = {"APCA-API-KEY-ID":api_key, "APCA-API-SECRET-KEY": api_secret}

# get account status
account = api.get_account()
porfolio_status(api)
market_time(api)