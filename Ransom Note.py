class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            index = magazine.find(c)
            if index == -1:
                return False
            if index == len(magazine) - 1:
                magazine = magazine[:len(magazine) - 1]
            else:
                magazine = magazine[:index] + magazine[index + 1:]
      
        return True
