class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        res = []
        while i<len(numbers):
            j = i+1
            while j< len(numbers):
                if numbers[i] + numbers[j] == target:
                    res.append(i+1)
                    res.append(j+1)
                print(numbers[i],numbers[j], i,j)
                j+=1
            print(res)
            i+=1
        return res
