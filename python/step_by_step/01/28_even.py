# coding: utf-8

from math import sqrt, ceil

a, b = map(int, input().split())

if a == b:
    if sqrt(a) ** 2 == a:
        print(0)
    else:
        print(1)
else:
    result = b - a + 1
    a = ceil(sqrt(a))
    b = ceil(sqrt(b))
    
    result -= b - a 
    print(result)

