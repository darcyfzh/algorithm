'''
@Author: Darcy
@Date: May, 18,2017
@Topic: Is tree2 is the subtree of pTree1
'''
from binarytree import *
def hasSubTree(pTree1, pTree2):
	result = False
	if pTree1 is not None and pTree2 is not None:
		if pTree1.value == pTree2.value:
			result = doesTree1HasTree2(pTree1, pTree2)
		if not result:
			result = hasSubTree(pTree1.left, pTree2)
		if not result:
			result = hasSubTree(pTree1.right, pTree2)
	return result

def doesTree1HasTree2(pTree1, pTree2):
	if pTree1 is None:
		return False
	if pTree2 is None:
		return True
	result = doesTree1HasTree2(pTree1.left, pTree2.left) and doesTree1HasTree2(pTree1.right, pTree2.right)
	return result
if __name__ == "__main__":
	nums1 = [int(i) for i in raw_input().strip().split()]
	nums2 = [int(i) for i in raw_input().strip().split()]
	pTree1 = convert(nums1)
	pTree2 = convert(nums2)
	result = hasSubTree(pTree1, pTree2)
	print result
