class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        mp -> val:i
        """
        dictt = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff not in dictt:
                dictt[n] = i
            else:
                return [dictt[diff],i]
        