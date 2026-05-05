class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s)==Counter(t)//time complexity O(n+m)
        # return sorted(s)==sorted(t)//O(nlogn)


        sdict = {}
        for ch in s:
            if ch not in sdict:
                sdict[ch] = 1
            else:
                sdict[ch] += 1
        tdict = {}
        for ch in t:
            if ch not in tdict:
                tdict[ch] = 1
            else:
                tdict[ch] += 1
        return sdict == tdict