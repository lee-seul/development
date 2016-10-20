# coding: utf-8

l1 = []
l2 = []
for i in range(3):
    a, b = map(int, input().split())
    l1.append(a)
    l2.append(b)

l1.sort()
l2.sort()

if l1[0] == l1[1]:
    a = l1[2]
else:
    a = l1[0]

if l2[0] == l2[1]:
    b = l2[2]
else:
    b = l2[0]

print(a, b)

