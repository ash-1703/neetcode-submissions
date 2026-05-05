class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for i in range(len(s)):
            if s[i] not in sd:
                sd[s[i]] = 1
                
            else:
                sd[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in td:
                td[t[i]] = 1
            else:
                td[t[i]] += 1
       

        return sd == td