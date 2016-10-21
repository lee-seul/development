# coding: utf-8
l = []
l = list(map(int, input().split()))

x = l[1] - l[0]
for i in range(len(l)-1):
    if l[i] + x != l[i+1]:
        x = l[1]//l[0]
        l.append(l[3]*x)
        break
if len(l) != 5:
    l.append(l[3] + x)

for i in l:
    print(i, end=" ")

