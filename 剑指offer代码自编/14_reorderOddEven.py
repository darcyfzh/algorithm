def reorderOddEven(a):
	low = 0;
	high = len(a) - 1
	while(low < high):
		while(low < high and a[low] % 2 != 0):
			low += 1
		while(low < high and a[high] % 2 == 0):
			high -= 1
		if(low < high):
			temp = a[low]
			a[low] = a[high]
			a[high] = temp
	return a
print reorderOddEven([1,3,2,4])