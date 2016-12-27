# coding: utf-8

import collections

def default_aa():
    return "aa"

dic = collections.defaultdict(default_aa, n1='hi')
print(dic)
print(dic['n2'])
