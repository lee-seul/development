# coding: utf-8

def swap():
    a, b = map(int, input().split())
    c = a
    a = b
    b = c
    print(a, b)

swap()
