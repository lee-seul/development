# coding: utf-8
# prime_10001st.py

def find_prime(num):
#l = []
	i = 1
	j = 1
	r = 0
	while(r<num):
		i +=1
		j = 1
		while(True):
			j += 1
			if i % j != 0:
				continue
			elif i % j == 0:
				if i == j:
#					l.append(i)
					r += 1
					break
				else:
					break
	return i
#	return l	
		
print(find_prime(10001))


		
