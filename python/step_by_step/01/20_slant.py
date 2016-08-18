# coding: utf-8

def slant():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    x = abs((b-d)//(a-c))
    print(x, b - (a * x))


slant()
