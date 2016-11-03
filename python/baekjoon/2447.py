# coding: utf-8

from math import log

n = int(input())
k = int(log(n, 3))
matrix = [["*" for col in range(n)] for row in range(n)]
line = ""
if n == 243:
    k = 5
for cnt in range(1, k+1):
    m = 3 ** cnt; x = m//3; y = m/3 * 2
    loop = [i for i in range(0, n) if i % m >=x and i % m < y]
    for row in loop:
        for col in loop:
            matrix[row][col] = " "

for row in range(n):
    line += "".join(matrix[row]) + "\n"        

print(line, end="")


