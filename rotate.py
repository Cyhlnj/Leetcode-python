class Solution:
	def rotate(self, nums, k):
		while k > 0:
			nums.insert(0, nums.pop())
			k -= 1
a=Solution()
k=1
nums=[1,2,3]
a.rotate(nums,k)
print ("result:",nums)