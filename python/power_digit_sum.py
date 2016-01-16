# coding: utf-8
# power_digit_sum.py

def two_power_sum(num):
	two = str(2**num)
	sum = 0
	for x in two:
		sum += int(x)
	return sum


print(two_power_sum(1000))

