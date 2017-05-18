class Node(object):
	def __init__(self, a):
		self.val = a
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

def reverseListNode(pHead):
	pReverseHead = None
	pPrev = None
	pNode = pHead.head
	while pNode != None:
		pNext = pNode.next
		if pNext == None:
			pReverseHead = pNode
		pNode.next = pPrev
		pPrev = pNode
		pNode = pNext
	return pReverseHead

if __name__ == "__main__":
	nums = [int(i) for i in raw_input().strip().split()]
	linked_list = linkedList() 
	for i in range(len(nums)):
		linked_list.addLast(nums[i])
	reverseHead = reverseListNode(linked_list)
	print reverseHead.val





