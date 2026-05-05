class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = Counter(s)
        tcount = Counter(t)
        c = 0
        if len(s)!=len(t):
            return False
        for i in s:
            if scount[i]==tcount[i]:
                continue
            else:
                return False
        return True
        