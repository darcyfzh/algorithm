listNode* merge(listNode* pHead1, listNode* pHead2)
{
	if(pHead1 == NULL)
		return pHead2;
	if(pHead2 == NULL)
		return pHead1;
	listNode* pMergedHead = NULL;
	if(pHead1 -> m_value < pHead2 -> m_value)
	{
		pMergedHead = pHead1;
		pMergedHead -> m_next = merge(pHead1 -> m_next, pHead2);
	}
	else
	{
		pMergedHead = pHead2;
		pMergedHead -> m_next = merge(pHead1, pHead2 -> m_next);
	}
	return pMergedHead;
}

