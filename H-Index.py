class Solution:
    def hIndex(self, citations: List[int]) -> int:
        tempList = sorted(citations)
        length = len(citations)
        for i in tempList:
            if i >= length:
                return length
            else:
                length = length - 1
        return length