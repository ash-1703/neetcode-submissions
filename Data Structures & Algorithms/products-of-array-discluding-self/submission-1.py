class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        # lst = []
        # for i in range(0,len(nums)):
        #     prod = 1
        #     for j in range(0,len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             prod *= nums[j]
        #     lst.append(prod)
        # return lst
        # most efficent solution in O(n)
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix *= nums[i]
        return res