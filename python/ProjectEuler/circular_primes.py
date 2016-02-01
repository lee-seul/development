# coding: utf-8
# circular_primes.py

from math import sqrt

def is_prime(num):
	if num > 1:
		for i in range(2, (int(sqrt(num)))+1):
			if num % i == 0:
				return False
		return True
	else:
	  	return False

def is_circular_prime(num):
	num = str(num)
	length = len(num)
	for i in range(length):
		if not is_prime(int(num[i:]+num[:i])):
			return False
	return True

prime_list = []


for i in range(2, 1000001):
	if is_circular_prime(i):
		prime_list.append(i)


	
print(len(prime_list))





