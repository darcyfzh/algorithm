listNode* reverseList(listNode* pHead)
{
	listNode* pNode = pHead;
	listNode* pPrev = NULL;
	listNode* preverseHead = NULL;
	while(pNode != NULL)
	{
		listNode* pNext = pNode -> m_next;
		if(pNext == NULL)
			preverseHead = pNode;
		pPrev = pNode -> m_next;
		pPrev = pNode;
		pNode = pNext;
	}
	return preverseHead;
}
