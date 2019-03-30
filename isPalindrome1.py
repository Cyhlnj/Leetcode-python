# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def isPalindrome1(self, head):
		vals = []
		#head = ListNode(0)
		while head:
			vals += head.val,
			head = head.next
		return vals == vals[::-1]

a=Solution()
b=[1,2,1]
print ("result:",a.isPalindrome1(b))
