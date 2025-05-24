class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        index = 0
        letters = {}
        for c in magazine:
            if c == ransomNote[index]:
                index += 1
                if index == len(ransomNote):
                    return True
                continue
            if c not in letters.keys():
                letters[c] = 1
            else:
                letters[c] += 1
        while index != len(ransomNote):
            if ransomNote[index] not in letters.keys():
                return False
            letters[ransomNote[index]] -= 1
            if letters[ransomNote[index]] < 0:
                return False
            index += 1
            
        return True
