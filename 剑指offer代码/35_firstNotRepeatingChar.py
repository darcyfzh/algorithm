'''
@Author: Darcy
@Date: May, 19, 2017
@Topic: First not repeating char
'''
def firstNotRepeatingChar(a):
	dic = {}
	for i in range(len(a)):
		if a[i] not in dic:
			dic[a[i]] = 1
		else:
			dic[a[i]] += 1
	dicReverse = [(v, k) for k, v in dic.items()]
	for index, element in enumerate(dicReverse):
		if element[0] == 1:
			return element[1]

if __name__ == "__main__":
	a = [i for i in raw_input().strip().split()]
	print firstNotRepeatingChar(a)
