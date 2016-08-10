# coding: utf-8
# 01_005_triangle.py

def triangle():
    a, b = map(int, input().split())
    print("{:0.2f}".format(a*b/2))

triangle()
