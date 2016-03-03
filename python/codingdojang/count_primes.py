# coding: utf-8
# count_primes.py

from math import sqrt

def is_prime(num):
	if num > 1:
		for i in range(2, int(sqrt(num))+1):
			if num % i == 0:
				return False
		return True
	else:
		return False


count = 0
for i in range(2, 1001):
	if is_prime(i):
		count += 1

print(count)


