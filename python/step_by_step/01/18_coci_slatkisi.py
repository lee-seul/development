# coding: utf-8

def coci_slatkisi():
    a, b = map(int, input().split())
    b = 10 ** b
    if a % b >= b/2:
        a += b
    a -= a % b
    print(a)

coci_slatkisi()
