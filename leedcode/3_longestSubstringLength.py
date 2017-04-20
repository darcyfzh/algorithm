##最长不重复连续子串的大小
def lengthOfLongestString(s):
	start = maxlen = 0
	dic = {}
	for i in range(len(s)):
		if s[i] in dic and start <= dic[s[i]]:
			start = dic[s[i]] + 1
	    maxlen = max(maxlen,i - start + 1)
	    dic[s[i]] = i
	return maxlen
