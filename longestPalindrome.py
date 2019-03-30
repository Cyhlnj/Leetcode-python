import string
class Solution(object):
	def longestPalindrome(self, s):
		temp = [s.count(c) for c in string.ascii_letters]
		print (temp)
		return sum([i // 2 * 2  for i in temp]) + (1 in [i % 2 for i in temp])

a=Solution()
b="aaaaa"
result=int(a.longestPalindrome(b))
print ("result:",result)
