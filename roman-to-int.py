class Solution:
	def romanToInt(self, s):
		"""
		Accoriding to the [wiki] (https://en.wikipedia.org/wiki/Roman_numerals),
		there are only three special cases, which are I, X and C. Thus we only need
		to handle these cases when needed.
		"""
		
		result = 0
		for i in range(len(s) - 1, -1, -1):
			if s[i] == 'I':
				result += 1 if result < 5 else -1
			elif s[i] == 'V':
				result += 5
			elif s[i] == 'X':
				result += 10 if result < 50 else -10
			elif s[i] == 'L':
				result += 50
			elif s[i] == 'C':
				result += 100 if result < 500 else -100
			elif s[i] == 'D':
				result += 500
			else:
				result += 1000
		return result

a=Solution()
s="CD"
print("result:",a.romanToInt(s))