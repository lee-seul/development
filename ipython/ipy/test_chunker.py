# encoding: utf-8
# test_chunker.py

import pandas as pd
from pandas import Series


chunker = pd.read_csv('ch06/ex6.csv', chunksize=1000)

tot = Series([])

for piece in chunker:
	tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.order(ascending=False)
