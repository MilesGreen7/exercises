class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s):
                if c == s[i]:
                    i += 1
            else:
                return True
        return False
