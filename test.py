from alpaca_trade_api import StreamConn
from alpaca_trade_api.common import URL
 

ALPACA_API_KEY = "PKPDAL2ML8PWKACS9U4I"
ALPACA_SECRET_KEY = "Q2KDR7V9uuuzs531qNXp9OXO3wwVUWdPVmm0t8Je"
 
 
if __name__ == '__main__':
    conn = StreamConn(
        ALPACA_API_KEY,
        ALPACA_SECRET_KEY,
        base_url=URL('https://paper-api.alpaca.markets'),
        data_url=URL('https://data.alpaca.markets'),
        data_stream='alpacadatav1'
    )

    @conn.on(r'Q\..+')
    async def on_quotes(conn, channel, quote):
        print('quote', quote)
        
    conn.run(['alpacadatav1/Q.GOOG'])