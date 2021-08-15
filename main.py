import secrets
import alpaca_trade_api as tradeapi
from secrets import *


# Not needed but whatever
api_key_id = secrets.api_key_id
secret_key = secrets.secret_key
endpoint = secrets.endpoint




# Imagine if name equals main 
if __name__ == '__main__':
    api = tradeapi.REST(api_key_id, secret_key, endpoint)

    api.submit_order('SPY', 5, 'buy', 'market','day')
    print("Order complete")






"""
Strategies to implement

Supertrend
Squeeze momentum
bollinger bands

"""