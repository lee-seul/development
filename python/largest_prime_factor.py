# coding: utf-8
# largest_prime_factor.py



#def find_list(num):
#	l=[]
#	for i in range(2, num):
#		if num % (i-1) == 0:
#			l.append(i-1)
#
#	return i



def find_rargest_prime(number):
	l = []
	n = 2
	while number!=1:
		if number % n == 0:
			l.append(n)
			number = number/n
		else: 
			n += 1
	l.sort()
	return l

print find_rargest_prime(600851475143)[-1]

		

