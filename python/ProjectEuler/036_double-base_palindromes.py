# coding: utf-8
# double-base_palindromes.py


def check_palindrome(num):
	num = str(num)
	length = len(num)
	if num[0] == '0':
		num = num[2:]
		length = length-2
	for i in range(int(length/2)):
		if num[i] != num[length-1-i]:
			return False
	return True

sum = 0

for i in range(1, 1000001):
	if check_palindrome(i) and check_palindrome(bin(i)):
		sum += i

print(sum)
				



