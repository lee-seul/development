# coding: utf-8

x, y = map(float, input().split())

if x + 0.5 <= y and x % 5 == 0:
    y -= x + 0.5
    
print("{:.2f}".format(y))

    

