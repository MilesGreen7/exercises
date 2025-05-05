class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candyCount = len(ratings)
        prev = 0
        cur = 0
        i = 0
        while i < len(ratings):
            cur = 0
            k = i
            while k + 1 < len(ratings):
                if ratings[k] > ratings[k + 1]:
                    candyCount += k + 1 - i
                    k += 1
                else:
                    break
            cur = k - i
            if i > 0 and ratings[i] > ratings[i-1] and cur <= prev:
                newCur = prev + 1
                candyCount += newCur - cur
                cur = newCur
            if k != i:
                prev = 0
            else:
                prev = cur
            i = k + 1
        return candyCount