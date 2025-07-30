from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        if height == None or len(height) <= 1:
            return result
        start, end = 0, len(height) - 1
        while start < end:
            if height[start] <= height[end]:
                result = max(result, height[start] * (end - start))
                start += 1
            else:
                result = max(result, height[end] * (end - start))
                end -= 1
        return result
            
