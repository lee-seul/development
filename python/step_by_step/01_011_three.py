# coding: utf-8
# 01_011_three.py

def three():
    a = int(input())
    b = input()
    for i in range(2, -1, -1):
        print(a*int(b[i]))
    print(a*int(b))

three()
    
