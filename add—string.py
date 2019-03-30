class Solution(object):
    def addStrings(self, num1, num2):
        from itertools import zip_longest
        nums = list(zip_longest(num1[::-1], num2[::-1], fillvalue='0'))
        carry, res = 0, ''
        for digits in nums:
            d1, d2 = map(int, digits)
            carry, val = divmod(d1 + d2 + carry, 10)
            res = res + str(val)
        res = res if carry == 0 else res + str(carry)
        return res[::-1]