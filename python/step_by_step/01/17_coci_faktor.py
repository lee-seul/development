# coding: utf-8

from math import ceil

def coci_faktor():
    a, b = map(int, input().split())
    b -= 0.99
    print(ceil(a*b))

coci_faktor()
