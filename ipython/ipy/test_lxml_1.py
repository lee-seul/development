# coding: utf-8
# test_lxml_1.py

from lxml.html import parse
from urllib.request import urlopen

parsed = parse(urlopen('http://finance.yahoo.com/q?s=AAPL&fr=uh3_finance_web&uhb=uhb2'))

doc = parsed.getroot()
links = doc.findall('.//a')

l = []
l_content = {}
for i in range(len(links)):
	lnk = links[i]
	l.append(lnk.get('href'))
	l_content[lnk.text_content()] = lnk.get('href')


tables = doc.findall('.//table')

calls = tables[4]
pust = tables[3]

rows = calls.findall('.//tr')

def _unpack(row, kind='td'):
	elts = row.findall('.//%s' % kind)
	return [val.text_content() for val in elts]



from pandas.io.parsers import TextParser

def parse_options_data(table):
	rows = table.findall('.//tr')
	header = _unpack(rows[0], kind='th')
	data = [_unpack(r) for r in rows[1:]]
	return TextParser(data, names=header).get_chunk()

call_data = parse_options_data(calls)
put_data = parse_options_data(pust)

