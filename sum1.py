class Solution(object):
	def twoSum(self, nums, target):
		d = {}
		for i, num in enumerate(nums):
			n=0
			
			if target - num in d:
				n=n+1
				print ("---if-:",n)
				print ('i:',i)
				print ('num:', num)
				print ("d[target-num]:", d[target - num])
				return [d[target-num], i]
				
			d[num] = i
			print('d[num]:',d)
a=Solution()
b=[2,7,11,15]
print(a.twoSum(b,9))