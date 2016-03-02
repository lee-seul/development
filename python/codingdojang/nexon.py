# coding: utf-8
# nexon.py

def d(n):
	result = n
	for x in str(n):
		result += int(x)
	return result

total = sum([i for i in range(1, 5000)])
generator_total = sum(set([d(i) for i in range(1, 5000) if d(i)<5000]))

print(total-generator_total)

