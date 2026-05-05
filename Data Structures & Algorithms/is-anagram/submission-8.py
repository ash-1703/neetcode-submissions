class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        s_ = ''.join(s_sorted)
        t_ = ''.join(t_sorted)
        return s_==t_