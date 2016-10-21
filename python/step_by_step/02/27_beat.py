# coding: utf-8

s, d = map(int, input().split())

a = (s+d)//2
b = a - d

if b < 0 or (s + d) % 2 != 0 or (s-d) % 2 != 0:
    print("impossible")
else:
    print(a, b)


