# coding: utf-8

def cociIntersect(n):
    return (n * (n-1) * (n-2) * (n-3))/24

a = int(input())

print(int(cociIntersect(a)))

