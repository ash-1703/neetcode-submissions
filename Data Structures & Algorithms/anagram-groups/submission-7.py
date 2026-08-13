class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_={}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dict_:
                dict_[sorted_word] = []
            dict_[sorted_word].append(word)

        return list(dict_.values())