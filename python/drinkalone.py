# coding: utf-8

import time
import requests
from bs4 import BeatifulSoup

url = 'http://linktv.club/main/sub/2364/%ED%98%BC%EC%88%A0%EB%82%A8%EB%85%80-%EB%8B%A4%EC%8B%9C%EB%B3%B4%EA%B8%B0'

source = requests.get(url)
soup = BeatifulSoup(source.text, 'lxml')


# now.tm_wday



