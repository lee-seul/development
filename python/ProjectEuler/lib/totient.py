# coding: utf-8
# totient.py

from lib.gcb_lcm import gcb

def phi(num):
	result = 0
	for i in range(1, num+1):
		if gcb(num, i) == 1:
			result += 1

	return result

