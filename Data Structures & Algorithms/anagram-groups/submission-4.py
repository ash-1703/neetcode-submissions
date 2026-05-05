class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = defaultdict(list)
        for word in strs: #act
            key = ''.join(sorted(word)) #act
            dict_[key].append(word)
           
        return list(dict_.values())