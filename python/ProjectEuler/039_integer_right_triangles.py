# coding: utf-8
# integer_right_triangles.py


result_dic = {}

for p in range(3, 1001):
	result_list = []
	print(p)
	for b in range(1, p):
		for a in range(1, p-b):
			c = p-(a+b)
			if c < a or c < b:
				break
			elif a > b:
				break
			elif c **2 == a**2 + b**2:
				result_list.append([a, b, c])
	result_dic[p] = len(result_list)


key_list = list(result_dic.keys())
max_value = 0
result = 0
for key in key_list:
	if max_value < result_dic[key]:
		max_value = result_dic[key]
		result = key

print(result)




