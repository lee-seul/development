class A(object):
    def __init__(self):
        print("enter a")
        print("living a")

class B(A):
    def __init__(self):
        print("enter b")
        super().__init__()
        print("living b")

class C(A):
    def __init__(self):
        print("enter c")
        super().__init__()
        print("living c")

class D(B, C):
    def __init__(self):
        print("enter d")
        super().__init__()
        print("living d")

d = D()

