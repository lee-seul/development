# coding: utf-8
# smallest_multiple.py

#def smallest_multiple(num):
#	l = []
#	result = 1
#	for i in range(2, num+1):
#		l.append(i)
#	
#	for x in l:
#		for y in l:
#			if x == y:
#				continue
#			elif x > y:
#				if x % y == 0:
#					if y in l:
#						l.remove(y)
#	for j in l:
#		result = result * j
#	
#	anw = []
#	for k in range(20, result):
#		for h in l:
#			if k % h != 0:
#				break
#			else:
#				anw.append(k)
#	return anw
#
#print(smallest_multiple(20)[1])
#

def find_smallest(num):
	result = 1
	if num > 0:
		for i in range(1, num+1):
			for j in range(1, num+1):
				if (result*j) % i == 0:
					result *= j
					break
		print(result)
	else:
		return False
