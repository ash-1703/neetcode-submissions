class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. key observation:
        -for anagrams, if we sort the characters, they from the same words.
        2. plan
        -we can use a dictionary where the sorted string will be the key and 
        its values will be the string from strs
        3. steps:
        1. initialize an empty dictionary (grouped)
        2. for each word in string, compute its sorted version
        3. add the word to the list corresponding to its sorted version in the dictionary
        4. return all the values of the dictionary as the result
        """
        grouped = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(word)
        return list(grouped.values())



         