'''
@Author: Darcy
@Date: May, 17, 2017
@Topic: maximum of subarray
'''
def greatestSumOfSubArray(a):
	if a == None or a == []:
		return 0
	curSum = 0
	nGreatest = float('-inf')
	for i in range(len(a)):
		if curSum <= 0:
			curSum = a[i]
		else:
			curSum += a[i]
		if curSum > nGreatest:
			nGreatest = curSum
	return nGreatest

if __name__ == '__main__':
	a = [int(i) for i in raw_input().strip().split()]
	result = greatestSumOfSubArray(a)
	print result