'''
@Author: darcy
@Date: May, 18, 2017
@Topic: rebuild binary tree with preorder list and inorder list
@To import binarytree library ,you can use order: pip install binarytree
'''
from binarytree import pprint, Node
def constructTree(preOrder, inOrder):
  # 忽略参数合法性判断
  if len(preOrder) == 0 :
    return None
  # 前序遍历的第一个结点一定是根结点
  rootData = preOrder[0]
  root = Node(rootData)
  root.left = None
  root.right = None
  for i in range(0, len(inOrder)):
    if inOrder[i] == rootData:
      break
  # 递归构造左子树和右子树
  root.left = constructTree(preOrder[1 : 1 + i], inOrder[:i])
  root.right = constructTree(preOrder[1 + i:], inOrder[i+1:])
  return root
if __name__ == '__main__':
  pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
  mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
  root = constructTree(pre_order, mid_order)
  pprint(root)