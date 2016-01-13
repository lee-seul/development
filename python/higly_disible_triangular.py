# coding: utf-8
# highly_disible_triangular.py

tri_num = 1
num = 2



while(True):
	counts = 0
	tri_num += num
	num += 1
	for i in range(1, int(tri_num**0.5)+1):
		if tri_num % i == 0:
			counts += 1
	if counts > 250:
		print(tri_num)
		break
	else:
		print(counts)
			
