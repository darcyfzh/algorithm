int depth(binaryTreeNode* pRoot)
{
	if(pRoot == NULL)
		return 0;
	int left = depth(pRoot -> m_left);
	int right = depth(pRoot -> m_right);
	return (left > right) ? left + 1 : right +1;
}

bool isBalance(binaryTreeNode* pRoot)
{
	if(pRoot == NULL)
		return true
	int left = depth(pRoot -> m_left);
	int right = depth(pRoot -> m_right);
	int diff = right - left;
	if(diff > 1 || diff < -1)
		return false;
	return isBalance(pRoot -> m_left) && isBalance(pRoot -> m_right);
}
