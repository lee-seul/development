# coding: utf-8

a = list(map(int, input().split()))
l = sorted(a)
l2 = list(reversed(l))
if a == l:
    print("ascending")
elif a == l2:
    print("descending")
else:
    print("mixed")

