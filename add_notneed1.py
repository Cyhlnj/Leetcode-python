class Solution(object):
    def getSum(self, a, b):
        if a==0 :
             return b
        if b==0 :
             return a
        while b!=0:
            carry=a&b
            a=a^b
            b=carry<<1
        return a
    
m =Solution()
a=-1
b=1
print ("result:", m.getSum(a,b))