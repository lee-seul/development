# coding: utf-8
# daum.py

def find_shortest(number_list):
	result = 0
	min_val = max(number_list)-min(number_list)
	for i in range(len(number_list)-1):
		val = number_list[i+1] - number_list[i]
		if min_val > val:
			min_val = val
			result = i
	return print(number_list[result], number_list[result+1])

find_shortest([1, 3, 4, 8, 13, 17, 20])
