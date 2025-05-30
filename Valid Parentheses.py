class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for c in s:
            if c is ']':
                if len(arr) == 0 or arr.pop(-1) != '[':
                    return False
            elif c is ')':
                if len(arr) == 0 or arr.pop(-1) != '(':
                    return False
            elif c is '}':
                if len(arr) == 0 or arr.pop(-1) != '{':
                    return False
            else:
                arr.append(c)
        if len(arr) == 0:
            return True
        else:
            return False
