# coding: utf-8
# digit_fifth_powers.py


fifth_powers_dic = {}

for i in range(10):
	fifth_powers_dic[i] = i**5



def digit_fifth_powers(num):
	num_str = str(num)
	result = 0
	for i in range(len(num_str)):
		result += int(num_str[i])**5
	if num == result:
		return True
	else:
	 	return False

result = []
for i in range(2, 590491):
	val = digit_fifth_powers(i)
	if val:
		result.append(i)
	


print(sum(result))




