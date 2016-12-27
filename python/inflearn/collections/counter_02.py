# coding: utf-8


import collections


ct3 = collections.Counter(['a', 'b', 'c', 'b', 'd', 'a'])
ct4 = collections.Counter('aeroplane')

print(ct3)
print(ct4)
print(ct3+ct4)
print(ct3-ct4)
print(ct3&ct4)
print(ct3|ct4)
