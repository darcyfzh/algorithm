'''
@Author: Darcy
@Date: May, 17, 2017
@Topic: Find the number which times is more than one half
'''

# def getKLeastNUmbers(a, k):
# 	if a == None or a == [] or k <= 0 or k > len(a):
# 		return
# 	start = 0
# 	end = len(a) - 1
# 	index = partition(a, start, end)
# 	while index != k - 1:
# 		if index > k - 1:
# 			end = index - 1
# 			index = partition(a, start, end)
# 		else:
# 			start = index + 1
# 			index = partition(a, start, end)
# 	return a[:k]


# def partition(a, start, end):
# 	index = start
# 	pivot = a[start]
# 	for j in range(start + 1, end + 1):
# 		if a[j] <= pivot:
# 			index += 1
# 			a[index], a[j] = a[j], a[index]
# 	a[index], a[start] = a[start], a[index]
# 	return index

from heapq import *
def kLeastNumber(a, k):
	if len(a) < k or k <= 0 or a == [] or a == None:
		return
	output = []
	for i in range(len(a)):
		if i < k:
			heappush(output,a[i])
		else:
			if a[i] < nsmallest(1, output):
				heappop(output)
				heappush(output, a[i])
	return output

if __name__ == "__main__":
	a = [int(i) for i in raw_input().strip().split()]
	print getKLeastNUmbers(a, 3)




