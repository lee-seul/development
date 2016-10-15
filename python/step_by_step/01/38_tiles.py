# coding: utf-8

a, b = map(int, input().split())

whole = (a//8) * (b//8)
result = 0
if a%8: result += b//8
if b%8: result += a//8
if a%8 and b%8: result += 1

print("The number of whole tiles is {} part tiles is {}".format(whole, result))

