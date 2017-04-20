def isValid(nums):
	for i in range(9):
		dic1 = {}
	    dic2 = {}
	    dic3 = {}
	    for j in range(9):
	    	if nums[i][j] != '.':
	    		if dic1[nums[i][j]] == True:
	    			return False
	    		dic[nums[i][j]] == True
	    	if nums[j][i] != '.':
	    		if dic2[nums[j][i]] == True:
	    			return False
	    		dic[nums[j][i]] == True
	        if nums[i/3*3+j/3][i%3*3+j%3] != '.':
	        	if dic3[nums[i/3*3+j/3][i%3*3+j%3]] == True:
	        		return False
	        	dic3[nums[i/3*3+j/3][i%3*3+j%3]] = True
	return True


