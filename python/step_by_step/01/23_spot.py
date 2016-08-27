# coding: utf-8


def spot(d, p):
    if p == 0:
        return 0
    return -(d * (p / 100))
    

d = float(input())
p = float(input())

print("{:.3f}".format(spot(d, p)))


