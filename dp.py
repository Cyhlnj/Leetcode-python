class Solution:
	def rob(self, num):
		i, e = 0, 0
		for n in num:
			i, e = n+e, max(i,e)
			print("i:",i)
			print("e:",e)
			print("-------------")
		return max(i,e)
a=Solution()
b=[1,2,3,1]
print ("result:",a.rob(b))