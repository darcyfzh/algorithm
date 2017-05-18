void mirror(binaryTreeNode* pRoot)
{
	if(pRoot == NULL)
		return;
	if(pRoot -> m_left == NULL || pRoot -> m_right == NULL)
		return;
	binaryTreeNode* pTemp = pRoot -> m_left;
	pRoot -> m_left = pRoot -> m_right;
	pRoot -> m_right = pTemp;
	if(pRoot -> m_left)
		mirror(pRoot -> m_left);
	if(pRoot -> m_right)
		mirror(pRoot -> m_right);
}