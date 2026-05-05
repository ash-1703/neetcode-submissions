class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check for sequences
        setNums = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in setNums:
                length = 0
                while (n+length) in setNums:
                    length +=1
                    # print(n,length,setNums)
                longest = max(length, longest)

        return longest
        