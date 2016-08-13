# coding: utf-8
# 01_014_fuse.py

def fuse():
    a, b, c = map(int, input().split())
    result = 2 * (a * 1.5 + a * 1.0 + b *2.0 + c * 0.5)
    if result % 10: 
        result += 10 - result % 10
    print("{:.0f} amperes".format(result))

fuse()
    
