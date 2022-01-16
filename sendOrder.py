import pickle as pkl
import pandas as pd
from pandas.core.frame import DataFrame
import alpaca_trade_api as tradeapi

file = "LCIDbars.pkl"
df = pd.read_pickle(file) # read from current directory


'''Ye's account'''
# connecting alpaca_trade_api
api_key='PKLP7X7VL8J4YHAZVCQI'
api_secret='4bTXTMfBMN96g2Of3q6R94ei0bl808OiqW4QEBGn'
alpaca_endpoint = "https://paper-api.alpaca.markets"
api = tradeapi.REST(api_key,api_secret,alpaca_endpoint,api_version='v2')
'''Yu's account'''
api_key='PKPDAL2ML8PWKACS9U4I'
api_secret='Q2KDR7V9uuuzs531qNXp9OXO3wwVUWdPVmm0t8Je'
alpaca_endpoint = "https://paper-api.alpaca.markets"
api = tradeapi.REST(api_key,api_secret,alpaca_endpoint,api_version='v2')

''' Business Logic '''
import BackTest as bt


''' Logic End '''


api.submit_order(
			symbol='AAPL',
			qty=100,
			side='buy',
			type='market',
			time_in_force='day',
)

api.submit_order(
			symbol='AAPL',
			qty=100,
			side='sell',
			type='market',
			time_in_force='day',
)

'''
Bracket orders allow you to create a chain of orders that react to execution and stock price.
'''
# We could buy a position and add a stop-loss and a take-profit of 5 %
api.submit_order(
    symbol=symbol,
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc',
    order_class='bracket',
    stop_loss={'stop_price': symbol_price * 0.95,
               'limit_price':  symbol_price * 0.94},
    take_profit={'limit_price': symbol_price * 1.05}
)

# We could buy a position and just add a stop loss of 5 % (OTO Orders)
api.submit_order(
    symbol=symbol,
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc',
    order_class='oto',
    stop_loss={'stop_price': symbol_price * 0.95}
)
'''
Trailing stop orders allow you to create a stop order that automatically changes the stop price 
allowing you to maximize your profits while still protecting your position with a stop price.
'''
# Submit a trailing stop order to sell 1 share of Apple at a
# trailing stop of
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='sell',
    type='trailing_stop',
    trail_price=1.00,  # stop price will be hwm - 1.00$
    time_in_force='gtc',
)

# Alternatively, you could use trail_percent:
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='sell',
    type='trailing_stop',
    trail_percent=1.0,  # stop price will be hwm*0.99
    time_in_force='gtc',
)