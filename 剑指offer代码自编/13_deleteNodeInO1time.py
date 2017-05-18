'''
@Author: Darcy
@Date: May, 18, 2017
@Topic: delete node of linked list in O(1) time
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


def print_linked_list(head):
    while head is not None:
        print head.value, ' ',
        head = head.next
    print ''

def deleteNode(pList, pToBeDeleted):
	if pList is None or pToBeDeleted is None:
		return
	pHead = pList.head
	if pToBeDeleted.next is not None:
		pNext = pToBeDeleted.next
		pToBeDeleted.value = pNext.value
		pToBeDeleted.next = pNext.next

	elif pHead.next is None and pToBeDeleted is pHead:
		return None
	else:
		while pHead.next != pToBeDeleted:
			pHead = pHead.next
		pHead.next = None
	return pHead

if __name__ == "__main__":
	nums = [int(i) for i in raw_input().strip().split()]
	pList = linkedList() 
	for i in range(len(nums)):
		pList.addLast(nums[i])
	linked_list_1 = deleteNode(pList, pList.head.next)

# class Node(object):
# 	def __init__(self, a, next = None):
# 		self.value = a
# 		self.next = next

# def createLinkedList(arr):
# 	node = Node(arr[-1])
# 	for i in range(len(arr) - 2, -1, -1):
# 		node = Node(arr[i], node)
# 	return node
# def print_linked_list(head):
#     while head is not None:
#         print head.value, ' ',
#         head = head.next
#     print ''
# def deleteNode(pList, pToBeDeleted):
# 	if pList == None or pToBeDeleted == None:
# 		return
# 	pHead = pList
# 	if pToBeDeleted.next != None:
# 		pNext = pToBeDeleted.next
# 		pToBeDeleted.value = pNext.value
# 		pToBeDeleted.next = pNext.next

# 	elif pHead.next is None and pToBeDeleted == pHead:
# 		return None
# 	else:
# 		while pHead.next != pToBeDeleted:
# 			pHead = pHead.next
# 		pHead.next = None
# 	return pHead

# if __name__ == "__main__":
# 	node = createLinkedList([1,2,3,4,5])
# 	linked_list_1 = deleteNode(node, node.next.next)
# 	print_linked_list(linked_list_1)