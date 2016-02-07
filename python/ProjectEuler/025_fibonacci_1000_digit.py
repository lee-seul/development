# coding: utf-8
# fibonacci_1000_digit.py

fibonacci_list = [1, 1, 2]

i = 3
while(len(str(fibonacci_list[-1]))!=1000):
	fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
	i += 1


print(len(fibonacci_list))
