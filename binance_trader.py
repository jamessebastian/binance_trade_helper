from binance.client import Client
import config

client = Client(config.api, config.secret_key)


print('logged in')

#info = 	client.get_symbol_info('BNBBTC')
info = 	client.get_account()
bal = info['balances']
for b in bal:
	if float(b['free']) > 0:
		print (b)

#from binance.enums import *
# order = client.create_test_order(
#     symbol='BNBBTC',
#     side=Client.SIDE_BUY,
#     type=Client.ORDER_TYPE_MARKET,
#     quantity=100)
