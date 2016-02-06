# coding: utf-8
# X_number.py

from math import sqrt

def triangle_num(num):
	return (num*(num+1))/2


def is_pentagon(num):
	n = abs(num)
	p = (sqrt(1+24*n)+1)/6
	return p == int(p)


def pentagon_num(num):
	return int(num*(3*num-1)/2)

def is_hexagon(num):
	n = abs(num)
	p = (sqrt(1+8*n)+1)/4
	return p == int(p)



