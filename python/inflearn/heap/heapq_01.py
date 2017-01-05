# coding: utf-8

import heapq
from showHeap import show_tree

data = [2, 4, 5, 7, 3, 10]

heap = []

for n in data:
    print("%3d" % n)
    heapq.heappush(heap, n)
    show_tree(heap)
