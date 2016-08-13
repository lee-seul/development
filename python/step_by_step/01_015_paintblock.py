# coding: utf-8
# 01_015_paintblock.py

def paintblock():
    a, b, c = map(int, input().split())
    print(4*(sum([a, b, c]) - 6))

paintblock();
