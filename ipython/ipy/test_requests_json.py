# coding: utf-8
# test_rquests_json.py

import sys, json, requests
from html.parser import HTMLParser

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.strict = False
		self.convert_charrefs = True
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()


url = 'https://twitter.com/search?q=python%20pandas&src=typd'

resp = requests.get(url)

data = strip_tags(resp.text)

data = data.strip()
data = json.loads(data)



#struct = {}

#try:
#	dataform = str(resp.text).strip("'<>() ").replace("'\r\n", '"\\r\\n')
#	struct = json.loads(dataform)
#except:
#	print(repr(resp.text))
#	print(sys.exc_info())
