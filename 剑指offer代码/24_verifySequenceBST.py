'''
@Author: Darcy
@Date: May, 19, 2017
@Topic: Verify if the sequence is the postorder of binary search tree
'''
def verifySequenceBST(sequence):
	if sequence == None or sequence == []:
		return False
	root = sequence[-1]
	index = 0
	for i in range(len(sequence) - 1):
		if sequence[i] > root:
			index = i
			break
	for j in range(index, len(sequence) - 1):
		if sequence[j] < root:
			return False
	if index > 0:
		left = verifySequenceBST(sequence[:index])
	if index < len(sequence) - 1:
		right = verifySequenceBST(sequence[index:len(sequence) - 1])
	return right and left

if __name__ == "__main__":
	arr = [int(val) for val in raw_input().strip().split()]
	print verifySequenceBST(arr)
