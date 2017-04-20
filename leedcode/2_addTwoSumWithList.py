# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class listNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def AddTwoSum(list1,list2):
    Sum = head = listNode(0)
    carry = 0
    while list1 or list2 or carry:
        temp1 = list1.val if list1 else 0
        temp2 = list2.val if list2 else 0
        tempSum = temp1 + temp2 + carry
        head.next = listNode(tempSum % 10)
        head = head.next
        carry = tempSum // 10
        if list1:
            list1 = list1.next
        if list2:
            list2 = list2.next
    return Sum.next