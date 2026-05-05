class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        # sorted_ = list(sorted(d.keys(), key = lambda x: d[x], reverse = True))
        
        sorted_ = list(sorted(d.keys(), key = d.get,reverse = True)) # d.get  = given a key, returns a values
        return sorted_[:k]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        creating a dictionary with val:freq
        {1:1,2:2,3:3}
        if v>k, append it to the list and then return it
        """
        freq = {}
        res = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        sorted_elements = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        print(sorted_elements)
        return sorted_elements[:k]       