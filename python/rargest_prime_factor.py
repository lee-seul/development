# coding: utf-8
# rargest_prime_factor.py



#def find_list(num):
#	l=[]
#	for i in range(2, num):
#		if num % (i-1) == 0:
#			l.append(i-1)
#
#	return i

l = []

def find_rargest_prime(number,l):
	n = 2
	while number!=1:
		if number % n == 0:
			l.append(n)
			number = number/n
		else: 
			n += 1
	l.sort()
	return l

find_rargest_prime(600851475143, l)
print l[-1]

		

