from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        result = [0] * size
        dec_stack = [0]
        for i in range(1, size):
            while dec_stack and temperatures[i] > temperatures[dec_stack[-1]]:
                idx = dec_stack.pop()
                result[idx] = i - idx
            dec_stack.append(i)
        return result
    
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))



