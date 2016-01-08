# coding: utf-8
# multiples_3_5.py

def multiple_3_5(number):
	total = 0
	for i in range(number):
		if i % 3 == 0:
			total += i
		elif (i % 5 == 0)and (i % 15 != 0):			
			total += i
			
	print total

multiple_3_5(1000)
