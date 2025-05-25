class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charDict = {}
        for i in range(len(s)):
            if s[i] in charDict.keys():
                if charDict[s[i]] != t[i]:
                    return False
            elif t[i] in charDict.values():
                return False
            else:
                charDict[s[i]] = t[i]
        return True
