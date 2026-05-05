class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hp = {"}":"{", ")":"(","]":"["}
        for c in s:
            if c in hp:
                if stack and stack[-1]==hp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True 