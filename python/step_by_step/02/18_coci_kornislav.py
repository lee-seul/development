# coding: utf-8

l = list(map(int, input().split()))

l.sort()

print(min(l[0], l[1]) * min(l[2], l[3]))



