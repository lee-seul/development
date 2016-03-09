# coding: utf-8
# comparison_version.py


def comparison_version(version1, version2):
	ver1 = [int(i) for i in (str(version1)).split('.')]
	ver2 = [int(i) for i in (str(version2)).split('.')]
	length = min(len(ver1), len(ver2))
	for i in range(length):
		if ver1[i] != ver2[i]:
			if ver1[i] > ver2[i]:
				return print(version1 + ">" + version2)
			else:
				return print(version1 + "<" + version2)
	if len(ver1) != len(ver2):
		if length == len(ver1):
			return print(version1 + "<" + version2)
		else:
			return print(version1 + ">" + version2)
	else:
		return print(version1 + "==" + version2)



comparison_version('0.0.2', '0.0.1')
comparison_version('1.0.10', '1.0.3')
comparison_version('1.2.0', '1.1.99')
comparison_version('1.1', '1.0.1')
comparison_version('2.3.1', '2.3.1')
			
		
