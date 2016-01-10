# coding: utf-8
# sum_square_difference.py

def sum_square_diff(num):
	square_sum = 0
	sum_square = 0
	for i in range(1, num+1):
		square_sum += i**2

	for j in range(1, num+1):
		sum_square += j
	
	sum_square = sum_square**2

	print(sum_square - square_sum)

