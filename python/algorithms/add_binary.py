# coding: utf-8
# add_binary.py

# 원소가 n개인 두 배열 A, B에 저장된 두개의 n비트 이진수를 더하라.

A = [1, 0, 1, 0, 0, 1, 1, 1]
B = [1, 1, 1, 1, 0, 1, 0, 0]

n = len(A)

C = [0 for i in range(n+1)]
for i in range(n-1, -1, -1):
    x = i + 1
    C[x] += A[i] + B[i]
    if C[x] == 2:
        C[x-1] += 1
        C[x] = 0
    elif C[x] == 3:
        C[x-1] += 1
        C[x] = 1

print(C)
