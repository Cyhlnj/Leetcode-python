class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF   #long int的最大值
        MIN_INT = 0x80000000    #long int的最小值,-2147483648
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
    
m =Solution()
a=-1
b=1
print ("result:", m.getSum(a,b))