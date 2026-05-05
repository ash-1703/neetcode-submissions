class Solution:
    def isValid(self, s: str) -> bool:
        """
        if its an open bracket, we append it to the stack
        if its a closing bracket, we check if its equal to top of the stack.
        if it is we remove it else, we return False
        """
        mapping = {"}":"{" , ")":"(" , "]":"["}
        stack = []
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack