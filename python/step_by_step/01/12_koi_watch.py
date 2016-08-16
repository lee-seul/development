# coding: utf-8

def koi_watch():
    a, b, c = map(int, input().split())
    sec = int(input())
    h = sec//3600
    m = (sec - h*3600)//60
    s = sec - h * 3600 - m * 60
    a += h
    b += m
    c += s
    if c>=60:
        c -= 60
        b += 1
    if b>=60:
        b -= 60
        a += 1
    if a >= 24:
        a -= (a//24)*24
    print(a, b, c)

koi_watch()

