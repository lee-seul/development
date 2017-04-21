# coding: utf-8


class Node:

    def __init__(self, key, item):
        self.key = key
        self.item = item


class MaxHeap:

    def __init__(self):
        self.heap = [None]
        self.length = 0

    def push(self, node):
        self.length += 1
        idx = self.length
        if self.length != 1 and node.key > self.heap[idx//2].key:
            self.heap[idx] = self.heap[idx//2]
            idx //= 2
        
        self.heap.append(node)

    def pop(self):
        if not self.length:
            return
        idx = self.length
        
        node = self.heap[1]
        temp = self.heap[idx]
        self.length -= 1
        parent = 1
        child = 2

        while child <= self.length:
            if child < self.length and self.heap[child].key < self.heap[child+1].key:
                   child += 1

            if temp.key >= self.heap[child].key:
                break

            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2

        self.heap[parent] = temp
        return node

n1 = Node(10, 2)
n2 = Node(9, 2)
n3 = Node(3, 3)
n4 = Node(8, 5)
n5 = Node(5, 3)

m = MaxHeap()

m.push(n1)
m.push(n2)
m.push(n3)
m.push(n4)
m.push(n5)

for _ in range(5):
    data = m.pop()
    print(data.key)


