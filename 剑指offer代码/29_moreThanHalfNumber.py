'''
@Author: Darcy
@Date: May, 17, 2017
@Topic: Find the number which times is more than one half
'''

def moreThanHalfNum(numbers):
	start = 0
	end = len(numbers) - 1
	middle = len(numbers) / 2
	index = partition(numbers, start, end)
	while index != middle:
		if index < middle:
			start = index + 1
			index = partition(numbers, start, end)
		else:
			end = index - 1
			index = partition(numbers, start, end)
	result = numbers[middle]
	return result

def partition(a, start, end):
	index = start
	pivot = a[start]
	for j in range(start + 1, end + 1):
		if a[j] <= pivot:
			index += 1
			a[index], a[j] = a[j], a[index]
	a[index], a[start] = a[start], a[index]
	return index


if __name__ == "__main__":
	a = [int(i) for i in raw_input().strip().split()]
	print moreThanHalfNum(a)
