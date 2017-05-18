void deleteNode(listNode** pHead, listNode* pToBeDeleted)
{
	if(pHead == NULL || pToBeDeleted == NULL)
		return;
	if(pToBeDeleted -> m_next != NULL)
	{
		listNode* pNext = pToBeDeleted -> m_next;
		pToBeDeleted -> m_value = pNext -> m_value;
		pToBeDeleted -> m_next = pNext -> m_next;
		delete pNext;
		pNext = NULL;
	}
	else if(pHead == pToBeDeleted)
	{
		delete pToBeDeleted;
		pToBeDeleted = NULL;
		*pHead = NULL;
	}
	else
	{
		listNode* pNode = pHead;
		while(pNode -> m_next != pToBeDeleted)
		{
			pNode = pNode -> m_next;
		}
		pNode -> m_next = NULL;
		delete pToBeDeleted;
		pToBeDeleted = NULL;
	}
}