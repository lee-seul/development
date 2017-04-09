# coding: utf-8


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def level_order(self):
        queue = []
        queue.append(self)
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


t3 = Tree(3)
t4 = Tree(4)
t5 = Tree(5)

t2 = Tree(2, t4, t5)
t1 = Tree(1, t2, t3)

t1.inorder()
print()

t1.preorder()

print()
t1.postorder()

print()
t1.level_order()

