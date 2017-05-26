'''
@Author: Darcy
@Date: May, 19, 2017
@Topic: The sum of two elements from an array equals to a given number
'''

def findTwoNumbersWithSum(a, sum):
	a = sorted(a)
	low = 0
	high = len(a) - 1
	while low < high:
		curSum = a[low] + a[high] 
		if curSum == sum:
			return low, high
		elif curSum < sum:
			low	+= 1
		else:
			high -= 1

if __name__ == "__main__":
	a = [int(i) for i in raw_input().split()]
	print findTwoNumbersWithSum(a, 5)

