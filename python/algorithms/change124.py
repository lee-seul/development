# coding: utf-8
# change124.py

def count_digit(num):
    std = 3
    mul = 2
    while(True):
        if num>std:
            std += 3**mul
            mul += 1
        else:
            return mul - 1

def change124(num):
    answer = ""
    count = count_digit(num)
    minus = sum([3**i for i in range(1, count)]) + 1
    num -= minus
    last = str(2**(num%3))
    print(count, minus, num)
    for i in range(count-1, 0, -1):
        answer += str(2**(num//3**i))
        num //= 3
        print(answer)
    answer += last
    return answer


print(change124(10))
print(change124(39))
print(change124(38))
print(change124(67610194989))

