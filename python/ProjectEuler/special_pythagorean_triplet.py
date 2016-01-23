# coding:utf-8
# special_pythagorean_triplet.py

from math import sqrt

def find_special_pythagorean(num):
	k = 0
	for i in range(1, int(num/2)):
		for j in range(1, int(num/2)):
			k = i**2 + j **2
			if k % sqrt(k) == 0:
				if i + j + sqrt(k) ==1000 and i < j and j < sqrt(k):
					print(i*j*sqrt(k))

find_special_pythagorean(1000)
