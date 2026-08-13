class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        s_list = list(s)
        t_list = list(t)
        for i in s_list:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1
        
        for i in t_list:
            if i not in dict_t:
                dict_t[i] = 1
            else:
                dict_t[i] += 1
        return dict_s == dict_t