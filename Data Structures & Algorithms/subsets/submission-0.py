class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol = [], []
        def backtrack(i):
            if i == len(nums):
                res.append(sol[:])
                return
            #dont pick the number
            backtrack(i+1)

            #pick the number
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            
        backtrack(0)
        return res