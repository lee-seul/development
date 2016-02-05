# coding: utf-8
# pentagon_numbers.py

from math import sqrt

def pentagon_num(num):
	return int(num*(3*num-1)/2)


def is_pentagon(num):
	n = abs(num)
	p =	(sqrt(1+24*n) +1)/6
	return p == int(p)


pentagon_list = []


n= 1

Not_found = True
while(Not_found):
	pentagon_list.append(pentagon_num(n))

	for j in range(2, len(pentagon_list)-1):
		if is_pentagon(pentagon_list[-1] + pentagon_list[j]) and is_pentagon(pentagon_list[-1] - pentagon_list[j]):
			print(abs(pentagon_list[j] - pentagon_list[-1]))
			Not_found = False
	n += 1
				





