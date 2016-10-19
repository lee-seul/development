# coding: utf-8

a, b = map(int, input().split())

ar = ''
br = ''
if a % 2 == 0:
    ar = "even"
else:
    ar = "odd"

if b % 2 == 0:
    br = "even"
else:
    br = "odd"

if ar == br:
    print("{}+{}={}".format(ar, br, "even"))
else:
    print("{}+{}={}".format(ar, br, "odd"))

if ar == "even" or br == "even":
    print("{}*{}={}".format(ar, br, "even"))
else:
    print("{}*{}={}".format(ar, br, "odd"))
