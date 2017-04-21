# coding: utf-8


class Node:

    def __init__(self, key, data, leftNode=None, rightNode=None):
        self.key = key
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode
    
    def isLeaf(self):
        return not self.leftNode and not self.rightNode

    def hasLeft(self):
        return not (self.leftNode is None)

    def hasRight(self):
        return not (self.rightNode is None)
    

class BinarySearchTree:

    def __init__(self, root=None):
        self.root= root
        self.size = 0
        if root:
            self.size = 1
        

    def search(self, key):
        temp = self.root
        while temp:
            if temp.key == key:
                return self.root
            if temp.key > key:
                temp = temp.leftNode
            else:
                temp = temp.rightNode
        return None

    def insert(self, key, data):
        if not self.search(key):
            temp = self.root
            
            while temp:
                if temp.key > key:
                    if not temp.hasLeft():
                        temp.leftNode = Node(key, data)
                        self.size += 1
                        break
                    else:
                        temp = temp.leftNode    

                else:
                    if not temp.hasRight():
                        temp.rightNode = Node(key, data)
                        self.size += 1
                        break
                    else:
                        temp = temp.rightNode


    def delete(self, key):
        if self.size > 1:
            temp = self.root
            while temp:
                if temp.leftNode and temp.leftNode.key == key:
                    temp.leftNode = None
                    self.size -= 1
                    break
                if temp.rightNode and temp.rightNode.key == key:
                    temp.rightNode = None
                    self.size -= 1
                    break
                
                if temp.key > key:
                    temp = temp.leftNode
                else:
                    temp = temp.rightNode

    def getLength(self):
        return self.size


