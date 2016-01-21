# coding: utf-8
# non-abundant_sums.py

def divisors_sum(num):
	divisor_sum = 0
	for i in range(1, int((num/2)+1)):
		if num % i == 0:
			divisor_sum += i
	if num < divisor_sum:
		return True

numbers = []
for i in range(12, 28124):
	if divisors_sum(i):
		numbers.append(i)
	
abundant_num = []
for x in range(len(numbers)):
	print(numbers[x])
	for y in range(len(numbers)):
#		print(numbers[x] + numbers[y])
#		if numbers[x] <= numbers[y]:
		if numbers[x] + numbers[y] <= 28123:
			abundant_num.append(numbers[x]+numbers[y])
		else:
			break
#		else:
#			break
#print(abundant_num)

abundant_num = set(abundant_num)
abundant_sum = 0

for x in abundant_num:
	abundant_sum += x

result = 0

for k in range(1, 28124):
#	if k not in abundant_num:
#		result += k
	result += k
print(result-abundant_sum)


#for k in range(1, 28124):
#	print(k)
#	if k < 24:
#		result += k
#	else:
#		for l in numbers:
#			if k > l:
#				if (k-l) not in numbers:
#					if l == number[-1]:
#						result += k
#				else:
#				 	break
#			else:
#			  break
			


