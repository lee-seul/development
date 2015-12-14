# encoding: utf-8
# test_csv_reader.py

import csv

f = open('ch06/ex7.csv')

reader = csv.reader(f)


lines = list(reader)

header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}

class my_dialect(csv.Dialect):
	lineterminator = '\n'
	delimiter = ';'
	quotechar = '"'
	quoting = csv.QUOTE_ALL

reader = csv.reader(f, dialect=my_dialect)

with open('my_data.csv', 'w') as f:
	writer = csv.writer(f, dialect=my_dialect)
	writer.writerow(('one', 'two', 'three'))
	writer.writerow(('1', '2', '3'))
	writer.writerow(('4', '5', '6'))
	writer.writerow(('7', '8', '9'))
