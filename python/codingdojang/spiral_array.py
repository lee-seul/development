# coding: utf-8
# spiral_array.py

import numpy as np

def make_spiral_array(a, b):
	array = np.zeros((a, b))
	i = 0
	x, y = 0, 0
	k, j = a, b
	c, d = -1, 0
	p = 0
	while(i!=a*b):
		array[x][y] = i
		i += 1
		if p == 0:
			y += 1
			if y == k:
				p = 1
				y = k - 1
				x += 1
				k -= 1
		elif p == 1:
			x += 1
			if x == j:
				p = 2
				x = j - 1
				y -= 1
				j -= 1
		elif p == 2:
			y -= 1
			if y == c:
				p = 3 
				y = c + 1
				x -= 1
				c += 1
		elif p == 3:
			x -= 1
			if x == d:
				p = 0
				x = d + 1
				y += 1
				d += 1
	return array

print(make_spiral_array(6,6))
