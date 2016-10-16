# coding: utf-8

m, n = map(int, input().split())


if m != 0 and n % m == 0:
    print("{} | {}".format(m, n))
else:
    print("{} !| {}".format(m , n))


