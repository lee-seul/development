# coding: utf-8

def op():
    a, b = map(int, input().split())
    print("{0}+{1}={2}".format(a, b, a+b))
    print("{0}-{1}={2}".format(a, b, a-b))
    print("{0}*{1}={2}".format(a, b, a*b))
    print("{0}/{1}={2}".format(a, b, int(a/b)))
    print("{0}%{1}={2}".format(a, b, a%b))

op()

