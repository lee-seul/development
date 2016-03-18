# coding: utf-8
# matrix_sum.py

def return_index(num, all_list):
	for i in range(len(all_list)):
		if all_list[i] == num:
			return i

def return_row(index):
	return int(index/15)
	
def return_col(index):
	return index%15

f = open('matrix.txt').read().split('\n')

matrix = []
for string in f:
	matrix.append(string.split(' '))

del matrix[-1]

all_list = []
sort_list = []

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		matrix[i][j] = int(matrix[i][j])
		all_list.append(matrix[i][j])
		sort_list.append(matrix[i][j])

sort_list.sort()
sort_list.reverse()

row_list = []
col_list = []
print(sort_list)
total = 0
for num in sort_list:
	index = return_index(num, all_list)
	all_list[index] = 0
	row_val = return_row(index)
	col_val = return_col(index)
#	print(index)
	if row_val not in row_list and col_val not in col_list:
		total += num
		row_list.append(row_val)
		col_list.append(col_val)
		print(num,row_val, col_val)

print(total)

	
