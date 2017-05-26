'''
@Author: Darcy
@Date: May, 19, 2017
@Topic: Two numbers appear once
'''
def findNumsAppearOnce(a):
	if a == [] or a == None:
		return
	exclusiveOR = 0
	for i in range(len(a)):
		exclusiveOR ^= a[i]
	indexOf1 = findFirstBitIs1(exclusiveOR)
	num1 = num2 = 0
	for j in range(len(a)):
		if isBit1(a[j], indexOf1):
			num1 ^= a[j]
		else:
			num2 ^= a[j]
	return num1, num2

def findFirstBitIs1(num):
	index = 0
	while num & 1 == 0:
		num = num >> 1
		index += 1
	return index

def isBit1(a, b):
	a = a >> b
	return a & 1

if __name__ == "__main__":
	a = [int(i) for i in raw_input().split()]
	print findNumsAppearOnce(a)
