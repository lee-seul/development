# coding: utf-8
# test_pandas_1.py

import pandas.io.data as web

all_data = {}

for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
	try:
		all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

		price = DataFrame({tic: data['ADj Close']
				for tic, data in all_data.iteritems()})

		volume = DataFrame({tic: data['Volume']
				for tic, data in all_data.iteritems()})

	except:
		print("Can't find ", ticker)
