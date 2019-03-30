class Solution():
	def maxProfit(self,prices):
		max_profit,min_price=0,99
		for  price in prices:
			min_price=min(min_price,price)
			profit =price-min_price
			max_profit=max(max_profit,profit)
			print("min_price:",min_price)
			print("max_profit:", max_profit)
			print("------------")
		return max_profit
	
class Solution1():
	def maxProfit1(self,prices):
		if not prices or len(prices) is 1:
			return 0
		profit =0
		
		max_profit,min_price=0,99
		for  price in prices:
			min_price=min(min_price,price)
			profit =price-min_price
			max_profit=max(max_profit,profit)
			print("min_price:",min_price)
			print("max_profit:", max_profit)
			print("------------")
		return max_profit
	
	
a=Solution()
b=[7,1,5,3,6,4]
print ("max:",a.maxProfit(b))
