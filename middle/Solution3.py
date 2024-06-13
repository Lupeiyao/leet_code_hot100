from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = -1
        start, end = 0, len(height) - 1
        while start < end:
            if height[start] < height[end]:
                max_val = max(max_val, height[start] * (end - start))
                start += 1
            else:
                max_val = max(max_val, height[end] * (end - start))
                end -= 1
        return max_val