from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        size = len(heights)
        inc_stack = []
        for i in range(size + 1):
            cur_height = heights[i] if i != size else 0
            while inc_stack and cur_height < heights[inc_stack[-1]]:
                height = heights[inc_stack.pop()]
                right = i - 1
                left = inc_stack[-1] + 1 if inc_stack else 0
                width = right - left + 1
                result = max(result, height * width)
            inc_stack.append(i)
        return result
    

print(Solution().largestRectangleArea([2,4]))
        

