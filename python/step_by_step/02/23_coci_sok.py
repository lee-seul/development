# coding: utf-8

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

m = 0
n = 0
while True:
    a -= x
    b -= y
    c -= z
    if a < x or b < y or c < z:
        dic = {a : a/x, b: b/y, c: c/z}
        dic_v = {a: x, b: y, c: z}
        for key in dic.keys():
            if min(dic.values()) == dic[key]:
                m = key
                n = dic_v[key]
        break

print("{:.6f} {:.6f} {:.6f}".format(a - (m * x/n), b - (m * y/n), c - (m * z/n)))
        


