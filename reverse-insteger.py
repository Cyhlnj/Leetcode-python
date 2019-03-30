



class Solution(object):
	def reverse(self, x):
		s=cmp(x,0)
		r = int("s*x"[::-1])    #先将字符串反转，然后将字符串转换为整型
		return s*r*(r<2**31)   #r < 2**31为真时返回1,否则返回0;2**31表示2的31次方
a=Solution()
b=123
print ("result:",a.reverse(b))