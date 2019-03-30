class Solution():
	def missnumber(self,nums):
		num_set=set(nums)
		n=len(nums)+1
		for i in range(n):
			if i not in num_set:
				return i


a=Solution()
b=[3,0,1]
print ("result:",a.missnumber(b))