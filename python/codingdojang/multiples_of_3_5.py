# coding: utf-8
# multiples_of_3_5.py

def multiple_3_5(number):
	return sum(set([i for i in range(number) if i % 3 == 0 or i % 5 == 0]))

print(multiple_3_5(1000))
