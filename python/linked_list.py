# coding: utf-8

class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data)

    def is_empty(self):
        if self.head is None:
            return True
        return False
 
    def length(self):
       	result = 0
        temp = self.head
        while temp:
            temp = temp.nextNode
            result += 1
        return result

    def search(self, pos):
        cnt = 0
        temp = self.head
        while cnt != pos - 1:
            temp = temp.nextNode
            cnt += 1
        return temp

    def add(self, data, pos):
        temp = self.search(pos)
        new_node = Node(data, temp.nextNode)
        temp.nextNode = new_node

    def delete(self, pos):
        temp = self.search(pos)
        temp.nextNode = temp.nextNode.nextNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.nextNode


l = LinkedList()
l2 = LinkedList(10)

print(l.head)
print(l2.head.data)

l2.head.nextNode = Node(20)

print(l2.head.nextNode.data)
print(l2.length())

l2.add(30, 2)
l2.add(40, 2)
l2.display()
print()
l2.delete(2)
l2.display()

