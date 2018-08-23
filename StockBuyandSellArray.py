class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        length = len(prices)
        for i in range(0,length-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
