'''
@Author: Darcy
@Date: May, 19,2017
@Topic: Mirror operation of binary tree
'''
from binarytree import *

def mirrorRecursively(pTree):
	if pTree is None:
		return
	if pTree.left is None and pTree.right is None:
		return
	pTemp = pTree.left
	pTree.left = pTree.right
	pTree.right = pTemp
	if pTree.left:
		mirrorRecursively(pTree.left)
	if pTree.right:
		mirrorRecursively(pTree.right)
	return pTree
if __name__ == "__main__":
	a = range(7)
	pTree = convert(a)
	mirrorRecursively(pTree)
	pprint(pTree)