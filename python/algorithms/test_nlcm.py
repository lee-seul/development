# coding: utf-8
# test_nlcm.py

def nlcm(num):
    num.sort()
    max_val = num[-1]
    while(True):
        count = 0
        for i in range(len(num)-1):
            if max_val % num[i] != 0:
                max_val += num[-1]
                break
            count += 1
        if count == len(num)-1:
             return max_val

print(nlcm([2,6,8,14]))
