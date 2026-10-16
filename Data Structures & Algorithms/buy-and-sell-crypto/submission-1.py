class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        sliding = []
        for i in range(1, len(prices)):
            buy = min(prices[:i])
            best = max(best, prices[i] - buy)
        
        return best


        