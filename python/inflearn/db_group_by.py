# coding: utf-8

from operator import itemgetter

rec_by_name = sorted(record, key=itemgetter('name'))

from itertools import groupby

for addr, items in groupby(records, key=itemgetter('addr')):
    

