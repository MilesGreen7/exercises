class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        leftPtr = 0
        rightPtr = len(height) - 1
        while leftPtr < rightPtr:
            tempWater = min(height[leftPtr], height[rightPtr]) * (rightPtr - leftPtr)
            maxWater = max(maxWater, tempWater)
            if height[leftPtr] > height[rightPtr]:
                rightPtr -= 1
            else:
                leftPtr += 1
        return maxWater
