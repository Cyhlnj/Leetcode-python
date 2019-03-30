class Solution(object):
    def mySqrt(self, x):
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

a=Solution()
b=4
print ("result:",a.mySqrt(b))