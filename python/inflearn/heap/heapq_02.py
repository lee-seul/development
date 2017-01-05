# coding: utf-8


import heapq
from showHeap import show_tree

data = [2, 5, 6, 10, 3, 4]

heapq.heapify(data)
show_tree(data)

min_val = heapq.heappop(data)
show_tree(data)
print(min_val)

# heapq.heapreplace()

heapq.nlargest(1, data)
heapq.nsmallest(2, data)
