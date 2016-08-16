# coding: utf-8

def paintblock():
    a, b, c = map(int, input().split())
    print(4*(sum([a, b, c]) - 6))

paintblock();
