struct listNode
{
	int m_value;
	listNode* m_next;
};

void printFromTailToHead(listNode* pHead)
{
	stack<*listNode> stack1;
	listNode* pNode = pHead;
	while(pNode != NULL)
	{
		stack1.push(pNode);
		pNode = pNode -> m_next;
	}
	while(!stack1.empty())
	{
		head = stack1.top();
		cout << head -> m_value;
		stack1.pop();
	}
}
