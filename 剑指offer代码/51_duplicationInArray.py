'''
@Author: Darcy
@Date: May, 20, 2017
@Topic: The repeating number in array
'''
def duplicationArray(arr):
	if arr == None or arr == []:
		return 
	duplication = []
	for i in range(len(arr)):
		while arr[i] != i:
			if arr[i] == arr[arr[i]]:
				duplication.append(arr[i])
			else:
				temp = arr[i]
				arr[i] = arr[temp]
				arr[temp] = temp
	return duplication

if __name__ == "__main__":
	a = [2,3,1,0,2,5,3]
	print duplicationArray(a)

