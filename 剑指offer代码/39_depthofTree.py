'''
@Author: Darcy
@Date: May, 19, 2017
@Topic: depth of the binary tree
'''
from binarytree import *
def depthOfTree(pTree):
	if pTree is None:
		return 0
	nLeft = depthOfTree(pTree.left)
	nRight = depthOfTree(pTree.right)
	if nLeft > nRight:
		return nLeft + 1
	else:
		return nRight + 1

# If a binary tree is binary balanced tree
def isBalanced(pTree):
	if pTree is None:
		return True
	elif:
		left = depthOfTree(pTree)
		right = depthOfTree(pTree)
		diff = right - left
		if diff > 1 or diff < -1:
			return false
	else:
		return isBalanced(pTree.left) and isBalanced(pTree.right)


if __name__ == "__main__":
	nums = [int(i) for i in raw_input().strip().split()]
	pTree = convert(nums)
	print depthOfTree(pTree)
