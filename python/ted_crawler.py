# coding: utf-8
# ted_crawler.py

import requests

from urlparse import urljoin
from scrapy.selector import Selector

def fetch_page(url):
	r = requests.get(url)
	return r.text

with open("ted_crawler.txt",'w') as f:
	html = fetch_page("http://www.ted.com/talks")
	f.write(html.encode('utf-8'))

def talk_links_from_listpage(url):
	html = fetch_page(url)
	sel = Selector(text=html)
	talk_links = sel.css('.talk-link .media__message a::attr(href)').extract()
	talk_links = [urljoin(url, talk_link) for talk_link in talk_links]
	return talk_links

from pprint import pprint

pprint(talk_links_from_listpage("http://www.ted.com/talks"))

