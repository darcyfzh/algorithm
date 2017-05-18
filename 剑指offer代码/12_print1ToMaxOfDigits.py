import itertools
def print1ToMaxOfDigits(digits):
	tupleList = []
	for i in range(digits):
		tupleList.extend(range(10))
	b = []
	for p in list(set(itertools.combinations(tupleList, 2))):
		b.append(list(p))
	for index, value in enumerate(b):
		if value[0] == 0:
			del(value[0])
	numList = []      
	for index, value in enumerate(b):
		numList.append(listToNum(value)) 
	return numList

def listToNum(array):
	num = 0
	for i in range(len(array)):
		num = num * 10 + array[i]
	return num

