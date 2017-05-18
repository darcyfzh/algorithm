bool HasSubTree(binaryTreeNode* pTree1, binaryTreeNode* pTree2)
{
	if(pTree1 != NULL && pTree2 != NULL)
	{
		if(pTree1 -> m_value == pTree2 -> m_value)
			result = doesTree1HasTree2(pTree1, pTree2);
		if(!result)
			result = HasSubTree(pTree1 -> m_left, pTree2);
		if(!result)
			result = HasSubTree(pTree1 -> m_right, pTree2);
	}
	return result;
}


bool doesTree1HasTree2(binaryTreeNode* pTree1, binaryTreeNode* pTree2)
{
	if(pTree1 == NULL || pTree2 == NULL)
		return false;
	if(pTree1 -> m_value != pTree2 -> m_value)
		return false;
	return doesTree1HasTree2(pTree1 -> m_left, pTree2 -> m_left) && 
	       doesTree1HasTree2(pTree1 -> m_right, pTree2 -> m_right);
}

