# coding: utf-8
# fibonacci.py

def fibonacci(number):
	a = 0
	b = 1
	while b<=number:
		a = b
		b = a+b
	return a

print(fibonacci(20))

		

