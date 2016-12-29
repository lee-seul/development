# coding: utf-8

import array
from pprint import pprint


string = "abcdefgh"

arr = array.array("u", string)
print(arr)

print(array.typecodes)
arr1 = array.array('i', range(5))
print(arr1)
arr1.extend(range(5))
print(arr1)

print(arr1[3:6])
print(list(enumerate(arr1)))
