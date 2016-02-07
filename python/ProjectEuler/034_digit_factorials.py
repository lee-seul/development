# coding: utf-8
# digit_factorials.py

def factorials(num):
	total = 1
	for i in range(1, num+1):
		total *= i
	return total


def num_to_list(num):
	num =  list(str(num))
	for i in range(len(num)):
		num[i] = int(num[i])
	return num

result = []

for i in range(3, 362880):
	fac_total = 0
	for j in num_to_list(i):
		fac_total += factorials(j)
	if i == fac_total:
		result.append(i)
	
print(sum(result))


