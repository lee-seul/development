# coding: utf-8

# 카운팅 소트
l = [0 for i in range(10001)]
n = int(input())

for i in range(n):
    num = int(input())
    l[num] += 1
loop = [i for i in range(1, 10001) if l[i] >0]

for index in loop:
    s = ""
    s += (str(index) + "\n") * l[index]
    print(s, end="")

