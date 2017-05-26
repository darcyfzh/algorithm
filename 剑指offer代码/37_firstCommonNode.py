'''
@Author: Darcy
@Date: May, 19, 2017
@Topic: First common node of two linkedList
'''
class Node(object):
	def __init__(self, a):
		self.value = a
		self.next = None

class linkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def length(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def addFirst(self, e):
		new = Node(e)
		if self.head == None:
			self.head = new
			self.size += 1
		else:
			new.next = self.head
			self.head = new
			self.size += 1

	def addLast(self, e):
		new = Node(e)
		if self.head == None:
			self.head = new
			self.size += 1
		else:
			prev = self.head
			while prev.next:
				prev = prev.next
			prev.next = new
			self.size += 1

def firstCommonNode(pList1, pList2):
	length_1 = pList1.length()
	length_2 = pList2.length()
	lengthDiff = length_1 - length_2
	pListLongHead = pList1.head
	pListShortHead = pList2.head
	if length_2 > length_1:
		lengthDiff = length_2 - length_1
		pListLongHead = pList2.head
		pListShortHead = pList1.head
	for i in range(lengthDiff):
		pListLongHead = pListLongHead.next
	while pListLongHead is not None and pListShortHead is not None and pListShortHead.value != pListLongHead.value:
		pListLongHead = pListLongHead.next
		pListShortHead = pListShortHead.next
	return pListLongHead.value

if __name__ == "__main__":
	nums1 = [int(i) for i in raw_input().strip().split()]
	nums2 = [int(i) for i in raw_input().strip().split()]
	pList1 = linkedList()
	pList2 = linkedList()
	for i in range(len(nums1)):
		pList1.addLast(nums1[i])
	for i in range(len(nums2)):
		pList2.addLast(nums2[i])
	print firstCommonNode(pList1, pList2)




