# coding: utf-8
# every_other_digit.py

def change_string(string):
	string = list(string)
	for x in range(len(string)):
		if x % 2 == 1 and string[x].isdigit():
			string[x] = '*'
	return ''.join(string)

print(change_string('a1b2cde3~g45hi6'))



