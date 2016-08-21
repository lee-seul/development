# coding: utf-8

def maxandmin(a, b):
    return max(min(a, b), a)

x, y = map(int, input().split())

print(maxandmin(x, y))

