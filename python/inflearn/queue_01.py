# coding: utf-8


import queue

q = queue.Queue()

for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())

lq = queue.LifoQueue()

for i in range(5):
    lq.put(i)

while not lq.empty():
    print(lq.get(), end=" ")

