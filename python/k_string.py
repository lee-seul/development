# coding: utf-8


def k_string(n, k):
    global A

    if n < 1:
        print(A)
    else:
        for j in range(k):
            A[n-1] = j
            k_string(n-1, k)


n, k = map(int, input().split())

A = [0 for _ in range(n)]
k_string(n, k)

