class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = 0
        i = 0
        nextIndex = None
        while i < len(haystack):
            if needle[k] == haystack[i]:
                k += 1
                if k == len(needle):
                    return i - (k - 1)
                elif k != 1 and nextIndex is None and needle[0] == haystack[i]:
                    nextIndex = i
            else:
                if k != 0:
                    k = 0
                    i -= 1
                if nextIndex is not None:
                    i = nextIndex - 1
                    nextIndex = None
                    
        return -1
        