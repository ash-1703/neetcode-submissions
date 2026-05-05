class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        #val:i
        """
        dict_={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dict_:
                dict_[nums[i]] = i
            else:
                return [dict_[diff], i]