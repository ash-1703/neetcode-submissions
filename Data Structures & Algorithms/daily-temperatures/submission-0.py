class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        0 - 30 -> 1 (1-0)
        1 - 38 -> 4 (5-1)
        2 - 30 -> 1 (3-2)
        3 - 36 -> 2 (5-3)
        4 - 35 -> 1 (5-4)
        5 - 40 -> 0 (0)
        6 - 28 -> 0 (0)
        """
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            j = i+1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                j+=1

        return res