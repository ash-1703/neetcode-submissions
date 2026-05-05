class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for i in nums:
        #     if i not in count:
        #         count[i] = 1
        #     else:
        #         count[i] += 1
        # sorted_list = list(sorted(count, key = lambda x: count[x], reverse = True))
        # return sorted_list[:k]
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        # {7:2}
        #count:i {2:7}
        freq = [[] for _ in range(len(nums)+1)]
        for n,c in dict_.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        









