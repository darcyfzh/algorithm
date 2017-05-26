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

def mergeTwoSortedList(pHead1, pHead2):
	if pHead1 is None:
		return pHead2 
	elif pHead2 is None:
		return pHead1
	pMergedHead = None
	if pHead1.value <= pHead2.value:
		pMergedHead = pHead1
		pMergedHead.next = mergeTwoSortedList(pHead1.next, pHead2)
	else:
		pMergedHead = pHead2
		pMergedHead.next = mergeTwoSortedList(pHead1, pHead2.next)
	return pMergedHead


if __name__ == "__main__":
	nums1 = [int(i) for i in raw_input().strip().split()]
	nums2 = [int(i) for i in raw_input().strip().split()]
	linked_list1 = linkedList()
	for i in range(len(nums1)):
		linked_list1.addLast(nums1[i])
	linked_list2 = linkedList()
	for i in range(len(nums2)):
		linked_list2.addLast(nums2[i])
	pHead1 = linked_list1.head
	pHead2 = linked_list2.head
	pMergedHead = mergeTwoSortedList(pHead1, pHead2)
	print pMergedHead.value