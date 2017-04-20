def search_rotated_Array(nums,target):
	low = 0
	high = len(nums) - 1
	mid = (high - low) / 2
	while low <= high:
	    if nums[mid] == target:
		    return mid
		if nums[low] < nums[mid]:
			if nums[low] <= target <= nums[mid]:
				high = mid - 1
			else:
				low = mid + 1
		else:
			if nums[mid] <= target <= nums[high]:
				low = mid + 1
            else:
            	high = mid - 1
    return -1


