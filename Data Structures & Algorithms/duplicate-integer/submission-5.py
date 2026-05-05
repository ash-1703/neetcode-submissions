class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_=set()
        for i in nums:
            if i not in set_:
                set_.add(i)
            else:
                return True
        return False