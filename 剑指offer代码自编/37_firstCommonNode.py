def firstCommonNode(list1, list2):
	len1 = len(list1)
	len2 = len(list2)
	if len1 > len2:
		diff = len1 - len2
		longList = list1
		shortList = list2
	else:
		diff = len2 - len1
		longList = list2
		shortList = list1
	longList = longList[diff:]
	i = 0
	while(longList[i] != shortList[i] and i <= len(shortList)):
		i += 1
	return shortList[i]
