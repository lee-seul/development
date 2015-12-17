# coding: utf-8
# test_lxml_2.py

from lxml import objectify
#from lxml.html import parse
#from urllib.request import urlopen

#parsed = parse(urlopen('http://www.mta.info/developers/download.html'))

path = 'Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []

skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE',
			'DECIMAL_PLACES']
	
for elt in root.INDICATOR:
	el_data = {}
	for child in elt.getchildren():
		if child.tag in skip_fields:
			continue
		el_data[child.tag] = child.pyval
	data.append(el_data)


from StringIO import StringIO

tag = <'a href="http://www.google.com">Google</a>'

root = objectify.parse(StringIO(tag)).getroot()


