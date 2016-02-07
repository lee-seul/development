# coding: utf-8
# amicable_numbers.py

def sum_divisors(num):
	total = 0
	for i in range(1, num):
		if num % i ==0:
			total += i
	return total 
	
dic = {}	

for i in range(1, 10001):
	dic[i] = sum_divisors(i)

print(dic)
#set_result = set()

result = 0
for i in range(1, 10001):
	for j in range(1, 10001):
		if i == j:
			continue
		elif dic[i] == j and dic[j] == i:
			result += i				# set_result.add(i)

#list_result = list(set_result)

#print(list_result)

#result = 0
#for i in list_result:
#	result += i

print(result)

