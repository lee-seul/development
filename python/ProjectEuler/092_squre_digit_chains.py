# coding: utf-8
# 092_square_digit_chains.py

def digit_square_sum(num):
	return sum([int(i)**2 for i in str(num)])


def make_list(num):
	limit = 9**2 * len(str(num))
	result_list = []
	for i in range(1, limit):
		n = i
		l = []
		while(True):
			l.append(n)
			if n == 89 or n in result_list:
				result_list+=l
				break
			elif n == 1:
				break
			else:
				n = digit_square_sum(n)
	return result_list


def count_digit_square_sum(num):
	count = 0
	result_list = make_list(num)
	for i in range(1, num):
		print(i)
		n = digit_square_sum(i)
		if n in result_list:
			count+=1
	return print(count)


count_digit_square_sum(10000000)


