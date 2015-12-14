# encoding: utf-8
# mydata.py

import csv

with open('my_data.csv', 'w') as f:
	writer = csv.writer(f, dialect=my_dialect)
	writer.writerow(('one', 'two', 'three'))
	writer.writerow(('1', '2', '3'))
	writer.writerow(('4', '5', '6'))
	writer.writerow(('7', '8', '9'))

