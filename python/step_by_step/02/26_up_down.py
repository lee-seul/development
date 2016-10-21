# coding: utf-8

l = []
for i in range(5):
    a = int(input())
    l.append(a)

nikky = 0
byron = 0
s = 0
cnt = -1

while l[4] > s:
    cnt += 1
    if cnt % 2 == 0:
        nikky += l[cnt%2]
    else:
        nikky -= l[cnt%2]
    s += l[cnt%2]

if l[4] < s:
    s -= l[4]
    if cnt % 2 == 0:
        nikky -= s
    else:
        nikky += s

cnt = -1
s = 0
while l[4] > s:
    cnt += 1
    if cnt % 2 == 0:
        byron += l[cnt%2 + 2]
    else:
        byron -= l[cnt%2 + 2]
    s += l[cnt%2 + 2]

if l[4] < s:
    s -= l[4]
    if cnt % 2 == 0:
        byron -= s
    else:
        byron += s

if byron > nikky:
    print("Byron")
elif byron == nikky:
    print("Tied")
else:
    print("Nikky")

