class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dict1 = {}
        lst = set()
        for i in strs:
            lst.add("".join(sorted(i)))
        for i in lst:
            dict1[i] = []
        for i in strs:
            if "".join(sorted(i)) in dict1:
                dict1["".join(sorted(i))].append(i)
        # print(lst)
        # print(sorted(list(dict1.values())))
        return sorted(list(dict1.values()))