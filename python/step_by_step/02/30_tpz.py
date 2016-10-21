# coding: utf-8

m = int(input())
a, b, c = map(int, input().split())

max_val = min(a, b, c)
min_val = m - ((m-a) + (m-b) + (m-c))

if min_val < 0:
    min_val = 0

print(max_val, min_val)


