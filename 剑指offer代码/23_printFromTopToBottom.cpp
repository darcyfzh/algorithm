void print(binaryTreeNode* pRoot)
{
	if(pRoot == NULL)
		return;
	deque<binaryTreeNode*> dequeTree;
	dequeTree.push_back(pRoot);
	while(dequeTree.size())
	{
		binaryTreeNode* pNode = dequeTree.front();
		dequeTree.pop_front();
		printf("%d", pNode -> m_value);
		if(pNode -> m_left)
			dequeTree.push_back(pNode -> m_left);
		if(pNode -> m_right
			dequeTree.push_back(pNode -> m_right);
	}
}