# coding: utf-8


import collections


print(collections.Counter(['aa', 'cc', 'dd', 'aa', 'bb', 'ee']))
print(collections.Counter({"가":3, "나":2, "다":4}))
print(collections.Counter(a=2, b=4, c=1))


container = collections.Counter()
print(container)
container.update("aabcdeffgg")
print(container)
container.update({'c':2, 'f':3})
print(container)

# Counter 접근하기
for n in "abdfe":
    print("%s: %d" % (n, container[n]))

ct = collections.Counter("Hello Jenny")
ct['x'] = 0
print(ct)

print(list(ct.elements()))

# most_common(in) 사용하기L 상위 n개를 시퀀스로 만든다.
ct2 = collections.Counter()
with open("test.txt", 'rt') as f:
    for li in f:
        ct2.update(li.rstrip())

for item, cnt in ct2.most_common():
    print("%s: %2d" %(item, cnt)) 
