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

def findkthToTail(pList, k):
	if pList is None:
		return None
	pAhead = pList.head
	pBehind = pList.head
	for i in range(k):
		if pAhead.next is not None:
			pAhead = pAhead.next
		else:
			return None
	while pAhead.next is not None:
		pAhead = pAhead.next
		pBehind = pBehind.next
	return pBehind

if __name__ == "__main__":
	nums = [int(i) for i in raw_input().strip().split()]
	pList = linkedList()
	for i in range(len(nums)):
		pList.addLast(nums[i])
	print findkthToTail(pList, 3).value

