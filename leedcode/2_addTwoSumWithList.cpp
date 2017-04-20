struct listNode
{
	int value;
	listNode* next;
};

listNode* addTwoSum(listNode* list1,listNode* list2)
{
	listNode* pNew(0);
	*temp = &pNew;
	int carry = 0
	while(list1 || list2 || carry)
	{
		temp1 = list1 ? list1 -> value : 0;
		temp2 = list2 ? list2 -> value : 0;
		tempSum = temp1 + temp2 + carry;
		temp -> next = new listNode(tempSum % 10);
		temp = temp -> next;
		carry = tempSum / 10;
		list1 = list1 ? list1 -> next : list1;
		list2 = list2 ? list2 -> next : list2;
	}
	return pNew	-> next;
}