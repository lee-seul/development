# coding: utf-8
# sum_prime.py


prime_list = [2]

def is_prime(num):
	for prime in prime_list:
		if num % prime == 0:
			return False
	prime_list.append(num)
	return True
			

				

def sum_prime(num):
	result = 2
	for i in range(3, num, 2):
		if is_prime(i):
			result += i
	return result


print(sum_prime(2000000))
