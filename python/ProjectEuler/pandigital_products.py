# coding: utf-8
# pandigital_products.py

standard_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
result_dic = {}
key_list = []
results = []


def num_to_str(num1, num2):
	mid = str(num1*num2)
	num1 = str(num1)
	num2 = str(num2)
	result = num1 + num2 + mid
	return result

str_list = []

for i in range(1, 100):
	for j in range(100, 4000):
		if '0' in str(i) or '0' in str(j) or '0' in str(i*j):
			continue
		else:
			str_list = list(num_to_str(i,j))
			str_list.sort()
			if standard_list == str_list:
 				result_dic[i*j] = num_to_str(i,j)  

#print(result_dic)

key_list = list(result_dic.keys())

print(sum(key_list))




