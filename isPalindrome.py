class Solution(object):
	def isPalindrome(self, x):
		return str(x) == str(x)[::-1]
		# s = cmp(x, 0)
		# r = int("s*x"[::-1])  # 先将字符串反转，然后将字符串转换为整型
		# ret =  s * r * (r < 2 ** 31)
		#
		# return ret    #r < 2**31为真时返回1,否则返回0;2**31表示2的31次方
a=Solution()
b= 999999999999999999999
print ("result:",a.isPalindrome(b))
