class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ans = 0, 0, 0
        res = set()
        
        while i < len(s) and j < len(s):
            if s[j] not in res:
                res.add(s[j])
                j += 1
                ans = max(ans, j - i) 
            else:
                res.remove(s[i]) 
                i += 1
        
        return ans