# coding: utf-8
# champernownes_constant.py


def champernownes(number):
	result = '0.'
	num = 1
	while(len(result)<=number+2):
		result += str(num)
		num+=1
	return int(result[number+1])

	
total = 1

l = [1, 10, 100, 1000, 10000, 100000, 1000000]

for i in l:
	total *= champernownes(i)

print(total)







