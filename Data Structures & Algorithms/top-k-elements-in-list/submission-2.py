class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
        return sorted_elements[:k]