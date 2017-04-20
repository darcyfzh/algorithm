def Search_Insert_Position(nums,k):
	if nums == None or nums == []:
		return 0
    low = 0
    high = len(nums) - 1
    while(low <= high):
        if k > nums[-1]:
        	return len
        if k < nums[0]:
        	return 0
        mid = (low + high) / 2
        midData = nums[mid]
        if midData == k:
            return k
        elif midData > k:
        	high = mid - 1
        	if nums[high] < k:
        		return high + 1
        else:
        	low = mid + 1
        	if nums[low] > k:
        		return low
        	