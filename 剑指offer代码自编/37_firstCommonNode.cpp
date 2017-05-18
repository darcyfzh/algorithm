listNode* find(listNode* pHead1, listNode* pHead2)
{
	int length1 = getlength(pHead1);
	int length2 = getlength(pHead2);
	listNode* pLong = pHead1;
	listNode* pShort = pHead2;
	int diff = length1 - length2;
	if(diff < 0)
	{
		diff = length2 - length1;
		pLong = pHead2;
		pShort = pHead1; 
	}
	for(int i = 0; i < diff; ++i)
	{
		pLong = pLong -> m_next;
	}
	while(pLong != NULL && pShort != NULL && pLong != pShort)
	{

		pLong = pLong -> m_next;
		pShort = pShort -> m_next;
	}
	listNode* pCommon = pLong;
	return pCommon
}

int getlength(listNode* pHead)
{
	int length = 0;
	listNode* pNode = pHead;
	while(pNode != NULL)
	{
		++length;
		pNode = pNode -> m_next;
	}
	return length;
}