class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordDict = {}
        indexStart = 0
        indexEnd = 1
        for c in pattern:
            if indexStart >= len(s):
                return False
            while indexEnd < len(s) and s[indexEnd] != ' ':
                indexEnd += 1
            if c in wordDict.keys():
                if wordDict[c] != s[indexStart : indexEnd]:
                    return False
            elif s[indexStart : indexEnd] in wordDict.values():
                return False
            else:
                wordDict[c] = s[indexStart : indexEnd]
            indexStart = indexEnd + 1
            indexEnd = indexStart + 1
        if indexStart < len(s):
            return False
        return True
