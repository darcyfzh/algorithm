#动态规划
def longestPalindromicSubstring(str):
	if str == None or str = [])：
		print "the length of string is at least 1"
	if len(str) == 1 or len(str) == 2:
		return str
	label = [[]]
	for i in range(0,len(str) - 1):
		label[i][i] = 1
		if i < length - 2 and str[i] == str[i + 1]:
			label[i][i + 1] = 1
			start = i
			maxlen = 2
	for i in range(3,len(str) + 1):
		for j in range(0, len(str) - i):
			m = j + i  - 1
            if label[j + 1][m - 1] and str[j] == str[m]:
            	label[j][m] = 1
            	maxlen = i
            	start = j
    if maxlen >= 2:
    	return str[i,i + maxlen - 1]


	
