# coding: utf-8
# likelion.py

def likelion(name):
	if isinstance(name, str):
		name.lower()
		if name=='seul':
			print(u"합격")
		else:
			print("????")

likelion('seul')
