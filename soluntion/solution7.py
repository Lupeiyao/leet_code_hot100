from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        if height is None or len(height) <= 2:
            return result 
        left, right = 1, len(height) - 2
        left_max, right_max = height[0], height[-1]
        while left <= right:
            if left_max <= right_max:
                result += max(left_max - height[left], 0)
                left_max = max(left_max, height[left])
                left += 1
            else:
                result += max(right_max - height[right], 0)
                right_max = max(right_max, height[right])
                right -= 1
        return result
    

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))