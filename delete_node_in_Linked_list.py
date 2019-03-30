class Solution():
	def deleteNode(self,node):
		if node.next:
			node.val=node.next.val
			node.next=node.next.next
		else:
			node.val = None
