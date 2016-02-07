# coding: utf-8
# spiral_diagonals.py


import numpy as np

def spiral_diagonals(num):
	spiral_list = np.zeros((num, num))
	x = 0
	y = num - 1
	z = 0
	n1 = 0
	n2 = num -1
	n3 = num -1
	n4 = 1
	value = num * num
	while(value!=0):
		spiral_list[x][y] = value
		if z == 0:
			y -= 1
			if y == n1:
				z = 1
				n1 += 1
		elif z == 1:
			x += 1
			if x == n2:
				z = 2
				n2 -= 1
		elif z == 2:
			y += 1
			if y == n3:
				z = 3
				n3 -= 1
		elif z ==3:
			x -= 1
			if x == n4:
				z = 0
				n4 += 1
		value -= 1
	return spiral_list

l = spiral_diagonals(1001)
total = 0



i = 0
j = 0
k = 1000
while(i!=1001):
	total += l[i][j] + l[i][k]
	i += 1
	j += 1
	k -= 1


print(total-1)



