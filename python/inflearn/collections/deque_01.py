# coding: utf-8


import collections

deq = collections.deque("hello python")
print(deq)
print(len(deq))
print(deq[0])
print(deq[-1])

deq.remove('o')
print(deq)

deq.append('a')
print(deq)

deq.appendleft('c')
print(deq)

print(deq.pop())
print(deq.popleft())
print(deq)

deq.extend('d')
print(deq)
deq.extendleft('a')
print(deq)

deq1 = collections.deque()
deq1.extend("abcdecf")

print(deq1)

deq1.extendleft('c')
print(deq1)

while True:
    try:
        print(deq1.pop(), end=' ')
    except IndexError:
        break
