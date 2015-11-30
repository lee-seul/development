# coding: utf-8
# test_np_where_2.py

result = []

for i in range(n):
	if cond1[i] and cond2[i]:
		result.append(0)
	elif cond1[i]:
		result.append(1)
	elif cond2[i]:
		result.append(2)
	else:
		result.append(3)


result1 = np.where(cond1 & cond2, 0, np.where(cond1, 1, np.where(cond2, 2, 3)))

result2 = 1 * (cond1 & -cond2) + 2 * cond2 & - cond1) + 3 * -(cond1 | cond2)

