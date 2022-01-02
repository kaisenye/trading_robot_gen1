'''
Web Connect Streamming retreive real-time stock data
'''

import alpaca_trade_api as tradeapi
from alpaca_trade_api import StreamConn
import threading
import time
import datetime
import logging
import argparse
# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig(
	filename='errlog.log',
	level=logging.WARNING,
	format='%(asctime)s:%(levelname)s:%(message)s',
)

# API KEYS
#region
'''Yu's account'''
api_key='PKPDAL2ML8PWKACS9U4I'
api_secret='Q2KDR7V9uuuzs531qNXp9OXO3wwVUWdPVmm0t8Je'
base_url = "https://paper-api.alpaca.markets"
data_url = 'https://data.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# init WebSocket
conn = tradeapi.stream2.StreamConn(
    api_key, api_secret, base_url=base_url, data_url=data_url, data_stream='alpacadatav1'
)


@conn.on(r'^T.AAPL$')
async def trade_info(conn, channel, bar):
	print('trade', bar)

@conn.on(r'^Q.AAPL$')
async def quote_info(conn, channel, bar):
    print('quote', bar)

@conn.on(r'^AM.AAPL$')
async def on_minute_bars(conn, channel, bar):
    print('bar', bar)


client_order_id = r'my_client_order_id'
@conn.on(client_order_id)
async def on_msg(conn, channel, data):
    # Print the update to the console.
    print("Update for {}. Event: {}.".format(client_order_id, data['event']))

# start websocket
def ws_start():
    conn.run(['trade_updates','AM.AAPL','Q.AAPL', 'T.AAPL'])


ws_thread = threading.Thread(target=ws_start, daemon=True)
ws_thread.start()

time.sleep(2)

