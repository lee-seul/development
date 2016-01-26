# coding: utf-8
# distinct_powers.py


result_list = []

for i in range(2, 101):
	for j in range(2, 101):
		result_list.append(i**j)

result = set(result_list)

print(len(result))


