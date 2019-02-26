class Solution:
	def addTwoNumbers(self, l1, l2):
		carry = 0
		root = n = ListNode(0)
		while l1 or l2 or carry:
			v1 = v2 = 0
			if l1:
				v1 = l1.val
				l1 = l1.next
			if l2:
				v2 = l2.val
				l2 = l2.next
				carry, val = divmod(v1+v2+carry, 10)
				n.next = ListNode(val)
				n = n.next
		return root.next
a=Solution()
L1=[2,4,3]
L2=[5,6,4]
print(a.addTwoNumbers(L1,L2))