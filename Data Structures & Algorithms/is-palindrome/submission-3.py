class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lst = []
        # for i in s:
        #     if i.isalnum():
        #         lst.append(i.lower())
        # word=''.join(lst)
        
        # return word == word[::-1]
        left = 0
        right = len(s)-1
        s = s.lower()
        # s_ = s_.alnum()
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
            