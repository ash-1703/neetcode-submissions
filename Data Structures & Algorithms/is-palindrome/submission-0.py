class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = (''.join(ch for ch in s if ch.isalnum())).lower()
        # print(a)
        return a == a[::-1]