class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # best = 0
        # sliding = []
        # for i in range(1, len(prices)):
        #     buy = min(prices[:i])
        #     best = max(best, prices[i] - buy)
        
        # return best
        min_price = prices[0]
        best = 0
        for price in prices[1:]:
            best = max(best, price - min_price)
            min_price = min(min_price, price)
        
        return best



        