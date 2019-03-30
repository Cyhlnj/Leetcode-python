class Solution(object):
    def moveZeroes(self, nums):
        zero=0
        for i in range(len(nums)):
            if not nums[i]==0 and zero<=i:
                nums[i],nums[zero]=nums[zero],nums[i]
                zero+=1
				
a=Solution()
b=[0,1,0,3,12]
print ("result:",a.moveZeroes(b))