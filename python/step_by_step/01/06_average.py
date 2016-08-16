# coding: utf-8

def average():
    a, b, c, d = map(int, input().split())
    print("{:.2f}".format(sum([a, b, c, d])/4))

average()
