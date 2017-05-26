'''
@Author: Darcy
@Date: 20, May, 2017
@Topic: The probablity of the dices
'''
from itertools import permutations
def probabilityDices(n, times, s):
	base = []
	for i in range(1, n + 1):
		base.append([i])
	count = 0
	while count < times- 1:
		new = []
		for i in range(len(base)):
			for j in range(1, n + 1):
				temp = base[i] + [j]
				new.append(temp)
		base = new
		count += 1
	arr = []
	for i, element in enumerate(base):
		if sum(element) == s:
			arr.extend(element)
	dic = {}
	for item in arr:
		if item in dic.keys():
			dic[item] += 1
		else:
			dic[item] = 1
	cases = n ** times
	for key in dic.keys():
		dic[key] = round(float(dic[key]) / cases, 3)
	return dic, cases



if __name__ == "__main__":
	#n, times, s = [int(i) for i in raw_input().split()]
	print probabilityDices(6, 4, 23)
