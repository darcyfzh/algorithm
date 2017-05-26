'''
@Author: Darcy
@Date: May, 26, 2017
@Topic:
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
the same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[[7], [2, 2, 3]] 
'''

def combinationSum(candidate, target):
	result = []
	sorted(candidate)
	def dfs(remain, stack):
		if remain == 0:
			result.append(stack)
			return
		for item in candidate:
			if item > remain:
				break
			if stack and item < stack[-1]: #To avoid duplicating terms
				continue
			dfs(remain - item, stack + [item])
	dfs(target, [])
	return result

print combinationSum([2,3,6,7], 7)






