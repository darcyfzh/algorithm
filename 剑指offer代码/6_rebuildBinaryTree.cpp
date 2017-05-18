binaryTreeNode* construct(int* preorder, int* inorder, int length)
{
	if(preorder == NULL || inorder == NULL || length == 0)
		return NULL;
	return constructCore(preorder, preorder + length - 1, inorder, inorder + length - 1);	
}

binaryTreeNode* constructCore(int* startPreorder, int* endPreorder, int* startInorder, int* endInorder)
{
	int rootValue = startPreorder[0];
	binaryTreeNode* root = new binaryTreeNode();
	root -> m_value = rootValue;
	root -> m_left = root -> m_right = NULL;
	int* rootInorder = startInorder;
	while(rootInorder <= endInorder && *rootInorder != rootValue)
		++ rootInorder;
	int leftLength = rootInorder - startInorder;
	int* leftPreorderEnd = startPreorder + leftLength;
	if(leftLength > 0)
		root -> m_left = constructCore(startPreorder + 1, leftPreorderEnd, startInorder, rootInorder - 1);
	if(leftLength < endPreorder - startPreorder)
		root -> m_right = constructCore(leftPreorderEnd + 1, endPreorder, rootInorder + 1， endInorder);
	return root;
}
