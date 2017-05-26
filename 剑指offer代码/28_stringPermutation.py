'''
@Author: Darcy
@Date: May, 17, 2017
@Topic: permutation sequence for an array
'''

def permutation(arr):
	if arr == None or arr == []:
		return
	support(arr, 0)

def support(arr, begin):
	if begin == len(arr):
		print arr
	for i in range(begin, len(arr)):
		temp = arr[i]
		arr[i] = arr[begin]
		arr[begin] = temp
		support(arr, begin + 1)
		temp = arr[i]
		arr[i] = arr[begin]
		arr[begin] = temp
permutation([1,2,3])
from itertools import combinations
def NQueens(n):
	arr = range(n)
	counts = 0
	for p in combinations(arr, n):
		result = check(p)
		if result:
			counts += 1
	return counts

def check(a):
	for i in range(len(a)):
		for j in range(i + 1, len(a)):
			if i - j == a[i] - a[j] or j - i == a[i] - a[j]:
				return False
	return True
print NQueens(8)




