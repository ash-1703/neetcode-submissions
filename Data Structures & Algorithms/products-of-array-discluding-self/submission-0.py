class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        # prod = 1
        lst = []
        for i in range(0,len(nums)):
            prod = 1
            for j in range(0,len(nums)):
                if i==j:
                    continue
                else:
                    prod *= nums[j]
            lst.append(prod)
        return lst