# coding: utf-8

import math

def rpoly(r, n):
    return n * (1/2 * (r * r * math.asin(math.radians(360/n))))

r, n = map(int, input().split())

print("{:.3f}".format(rpoly(r, n)))

