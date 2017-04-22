# coding: utf-8


def binary(n):
    global A

    if n < 1:
        print(A)
    else:
        A[n-1] = 0
        binary(n - 1)
        A[n-1] = 1
        binary(n - 1)

n = int(input())

A = [0 for _ in range(n)]
binary(n)

