class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) < 2:
            return res

        i = 0
        j = 1
        while j < len(prices):
            profit = prices[j] - prices[i]
            res = max(res, profit)
            if prices[j] < prices[i]:
                i = j
            j += 1
        return res 
