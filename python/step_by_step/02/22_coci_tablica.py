# coding: utf-8

a, b = map(int, input().split())
c, d = map(int, input().split())

l = []
for i in range(4):
    l.append(a/c + b/d)
    tmp = a
    a = c
    c = d
    d = b
    b = tmp

for i in range(len(l)):
    if max(l) == l[i]:
        print(i)
        break

