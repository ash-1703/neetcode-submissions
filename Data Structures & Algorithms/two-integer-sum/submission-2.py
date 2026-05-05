class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # i = 0
        # lst = []
        # while i<len(nums):
        #     j = i+1
        #     while j<len(nums):
        #         if nums[i]+nums[j] == target:
        #             lst.append(i)
        #             lst.append(j)
        #         j+=1
        #     i+=1
        # return lst
        '''
        nums = [3,4,5,6]
               [0,1,2,3]
        target = 7
        diff = 4,3
        '''
        hashmap = {} #val:index
        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return[hashmap[diff],i]
            hashmap[nums[i]] = i
            i+=1

            


           

         