# coding: utf-8
# isertion_sort.py

# 삽입 정렬

import time

# 입력 함수
t1 = time.time()
def input_list():
    num = input("수열의 길이 입력: ")
    num_list = []
    for i in range(int(num)):
        temp = input("숫자 입력: ") 
        num_list.append(int(temp))
    return num_list 

# 정렬 함수
def sort_list(num_list):
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i - 1
        while j > 0 and num_list[j] > key:
            num_list[j+1] = num_list[j]
            j = j - 1
        num_list[j+1] = key
    return print(num_list)


sort_list(input_list())

t2 = time.time()

print("{0} secondss".format(t2-t1))
