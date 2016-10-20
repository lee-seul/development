# coding: utf-8

l = list(map(int, input().split()))

l.sort()

if l[0] + l[1] > l[2]:
    print("yes")
else:
    print("no")



