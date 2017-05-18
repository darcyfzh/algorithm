listNode* findKthFromEnd(listNode* pHead, int k)
{
	if(pHead == NULL || k <= 0)
		return NULL;
	listNode* pAhead = pHead;
	listNode* pBehind = pHead;
	for(int i = 0; i < k - 1; ++i)
	{
		if(pAhead -> m_next != NULL)
			pAhead = pAhead -> m_next;
		else
			return NULL;
	}
	while(pAhead -> m_next != NULL)
	{
		pAhead = pAhead -> m_next;
		pBehind = pBehind -> m_next;
	}
	return pBehind;
}