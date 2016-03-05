# coding: utf-8
# make_largest_number.py


def make_largest_number(number_list):
	digit_list = []
	result = ''
	for num in number_list:
		if len(str(num)) > 1:
			for x in str(num):
				digit_list.append(int(x))
		else:
			digit_list.append(num)
	digit_list.sort()
	digit_list.reverse()
	for digit in digit_list:
		result += str(digit)
	return int(result)


print(make_largest_number([1,2,3]))
print(make_largest_number([3, 30, 34, 5, 9]))
