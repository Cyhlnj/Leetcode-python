class Solution(object):
    def addBinary(self, a, b):
       #return (bin(a)[2:] + bin(b)[2:])
       return  bin(eval('0b'+a) + eval('0b' + b))[2:]

m=Solution()
a="11"
b= "1"
print ("result:",m.addBinary(a,b))