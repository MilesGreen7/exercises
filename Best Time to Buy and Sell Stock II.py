class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        returnVal = 0
        for p in range(len(prices)):
            if p + 1 < len(prices) and prices[p+1] - prices[p] > 0:
                returnVal += prices[p+1] - prices[p]

        return returnVal