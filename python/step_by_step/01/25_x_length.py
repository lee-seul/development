# coding: utf-8

pi = 3.14159
a, b = map(int, input().split())

l1 = lambda x : x * pi
l2 = lambda x : (2 * (x ** 2)) ** (1/2)

print("{:.3f}".format(l1(a) + l1(b) + l2(a) + l2(b)))

