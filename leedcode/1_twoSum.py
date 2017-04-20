#Given an array of integers
#return indices of the two numbers such that they add up to a specific target.
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
def twoSum(nums,target):
	if len(nums <= 1):
		return False
	buffDic = {}
	for i in range(len(nums)):
		if nums[i] in buffDic:
			return [buffDic[num[i]],i]
		else:
			buffDic[target - num[i]] = i