'''
@Author: Darcy
@Date: May. 19,2017
@Topic: print the binary tree from top to printFromTopToBottom
'''
from binarytree import *
from collections import deque
def printFromTopToBottom(pTree):
	if pTree is None:
		return
	d = deque()
	d.append(pTree)
	while len(d):
		pNode = d.pop()
		print pNode.value
		if pNode.left:
			d.append(pNode.left)
		if pNode.right:
			d.append(pNode.right)

if __name__ == "__main__":
	nums = [int(i) for i in raw_input().strip().split()]
	pTree = convert(nums)
	printFromTopToBottom(pTree)