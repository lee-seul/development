# coding: utf-8

from math import sqrt, ceil


def is_right(prime ,num):
    count = 1
    idx = 0
    temp = 0
    while num > 1:
        #print(num)
        if num in prime:
            temp = 1
            break
        else:
            if num % prime[idx] == 0:
                num //= prime[idx]
                temp += 1
            else:
                idx += 1
                count *= temp + 1
                if temp + 1 % 2 == 0:
                    return False
                temp = 0
    count *= temp + 1
    return count % 2 == 1

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

a, b = map(int, input().split())

l = [0 for i in range(ceil(sqrt(b))+2)]
for i in range(2, len(l)):
    if l[i] == 0:
        n = 2
        while i*n <= ceil(sqrt(b))+1:
            l[i*n] = 1
            n += 1

prime = []
for i in range(2, len(l)):
    if l[i] == 0:
        prime.append(i)
#print(prime) 
bottom = b - a
top = 0
for i in range(a+1, b+1):
    if is_right(prime ,i):
        top += 1
div = gcd(bottom, top)

if top == 0:
    print(0)
else:
    print("{}/{}".format(top//div, bottom//div))
