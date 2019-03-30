class Solution(object):
	def removeDuplicates(self, A):
		if not A:
			return 0
		else:
			ii,jj=1,1
			while jj<len(A):
				if A[ii-1]!=A[jj]:
					A[ii]=A[jj]
					ii+=1
				jj+=1
			return ii


a=Solution()
b=[1,1,2]
print ("result:",a.removeDuplicates(b))