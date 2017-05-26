'''
@Author: Darcy
@Date: May, 26, 2017
@Topic:
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
def multiply_strings(str1, str2):
	str1 = list(str1)
	str2 = list(str2)
	assert (str1 != [] and str1 != None) and (str2 != [] and str2 != None)
	if str1 == '0' or str2 == '0':
		return 0
	if str1[0] = '0':
		str1 = str1[1:]
	if str2[0] == '0':
		str2 = str2[1:]
	if len(str1) > len(str2):
		longStr = str1
		shortStr = str2
	else:
		longStr = str2
		shortStr = str1
	result = 0
	for j in range(1,len(shortStr) + 1):
		muls = []
		temp = 0
		for i in range(1, len(longStr) + 1):
			mul = int(shortStr[-j]) * int(longStr[-i])
			mul += temp
			temp = mul / 10
			rem = mul % 10
			muls.append(rem)
		muls = list(reversed(muls))
		tmpSum = sumArr(muls) * (10 ** (j - 1))
		result += tmpSum 
	return result

def sumArr(arr):
	Sum = 0
	for item in arr:
		Sum = Sum * 10 + item
	return Sum 

print multiply_strings('12','12')


