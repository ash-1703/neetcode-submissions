class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False

        for i,v in enumerate(s):
            if v not in d1:
                d1[v] = 1
            else:
                d1[v] += 1

        for i,v in enumerate(t):
            if v not in d2:
                d2[v] = 1
            else:
                d2[v] += 1
        return d1 == d2
        
            