# coding: utf-8

import heapq

class PriorityQueue:
    def __init__(self):
        self.q = []
        self.idx = 0

    def put(self, item, priority):
        heapq.heappush(self.q, (priority, self.idx, item))
        self.idx += 1

    def pop(self):
        return heapq.heappop(self.q)

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)

pQ = PriorityQueue()

pQ.put(Item("홍길동"), 3)
pQ.put(Item("장길산"), 1)
pQ.put(Item("임꺽정"), 2)
pQ.put(Item("일지매"), 4)


for _ in range(4):
    print(pQ.pop())
