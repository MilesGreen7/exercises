class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxMoney = 0
        tempSum = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > tempSum + diff:
                tempSum = diff
            else:
                tempSum += diff
            if tempSum > maxMoney:
                maxMoney = tempSum
        return maxMoney