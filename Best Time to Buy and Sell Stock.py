class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestPrice = prices[0]
        maxMoney = 0
        for i in range(1, len(prices)):
            temp = prices[i] - bestPrice
            if prices[i] < bestPrice:
                bestPrice = prices[i]
            elif temp > maxMoney:
                maxMoney = temp
        return maxMoney