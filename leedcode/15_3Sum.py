#预处理，先对数组进行排序
def threeSum(nums):
	if len(nums) < 3:
		return 0
	elif len(nums) == 3:
		return sorted(nums)
	result = []
	nums = sorted(nums)
	for i in range(len(nums) - 2):
		j = i + 1
		k = len(nums) - 1
		while j < k:
			temp_sum = nums[i] + nums[j] + nums[k]
			if temp_sum == 0:
				nums.append((nums[i],nums[j],nums[k]))
			elif temp_sum < 0:
				j += 1
			else:
				k -= 1
	return list(set(result)) #result 形式是[(1,2),(1,2),(2,3)],不能是二维数组形式
print (threeSum([-1,1,0,2,3]))