def longestCommonPrefix(str):
	if str == [[]] or str == None:
		return ""
	for i,group in enumerate(zip(str)):
		if len(set(group)) > 1:
			return str[0][:i]
    else:
    	return min(str)