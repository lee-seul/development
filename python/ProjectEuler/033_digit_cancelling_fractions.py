# coding: utf-8
# digit_cancelling_fractions.py


def digit_cancelling(num1, num2):
	value = num1/num2
	num3 = list(str(num1))
	num4 = list(str(num2))
	for i in num3:
		if i in num4:
			num3.remove(i)
			num4.remove(i)
			if value == int(num3[0])/int(num4[0]):
				return [num1, num2]
	else:
	 	return False

result = []

for i in range(10, 99):
	for j in range(10, 99):
		if i % 10 == 0 or j % 10 == 0:
			continue
		elif i >= j:
			continue
		else:
			if digit_cancelling(i,j):
				result.append(digit_cancelling(i,j))

total1 = 1
total2= 1

for i in range(len(result)):
	total1 *= result[i][0]
	total2 *= result[i][1]

print(total1/total2)




