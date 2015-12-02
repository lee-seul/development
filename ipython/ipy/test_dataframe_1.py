# coding: utf-8
# test_dataframe_1.py

from pandas import DataFrame

data = {'State': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
	    'year': [2000, 2001, 2002, 2001, 2002],
		'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)
