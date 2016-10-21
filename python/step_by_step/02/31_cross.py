# coding: utf-8

a, b = map(int, input().split())
c, d = map(int, input().split())

if max(a, b) < max(c, d) and min(a,b) < min(c, d) and min(c, d) < max(a, b):
    print("cross")
elif max(a,b) > max(c, d) and min(a, b) < max(c, d) and min(a, b) > min(c, d):
    print("cross")
else:
    print("not cross")

