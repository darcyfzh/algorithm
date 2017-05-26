'''
@Author: Darcy
@Date: May, 26, 2017
@Topic: 
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''
import itertools
def countAndSay(n):
	s = '1'
	for i in range(n - 1):
		s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
	return s

print countAndSay(3)
