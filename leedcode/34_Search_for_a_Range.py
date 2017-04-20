def getFirstOfK(nums,k,low,high):
	if nums == None or nums == []:
	    return 0
	mid = (low + high) / 2
	middleData = nums[mid]
	if middleData == k:
	    if (mid > 0 and nums[mid - 1] != k) or (mid == 0):
	        return mid 
	    else:
	        high = mid - 1
	elif middleData < k:
	    low = mid + 1
	else:
	    high = mid - 1
	return getFirstOfK(nums,k,low,high)


def getLastOfK(nums,k,low,high):
    if nums == None or nums == []:
        return 0
    mid = (low + high) / 2
    middleData = nums[mid]
    if middleData == k:
        if (mid < len(nums) - 1 and nums[mid + 1] != k) or mid == len(nums) - 1:
           return mid 
        else:
            low = mid + 1
    elif middleData > k:
        high = mid - 1
    else:
        low = mid + 1
    return getLastOfK(nums,k,low,high)

def getNumOfK(nums,k):
    if nums == None or nums == []:
        return 0
    num = 0
    first = getFirstOfK(nums,k,0,len(nums) - 1)
    last = getLastOfK(nums,k,0,len(nums) - 1)
    num = last - first + 1
    return num 