from typing import List 


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        max_range = nums[0]
        idx = 1
        while idx <= max_range and idx <= size - 1:
            max_range = max(max_range, idx + nums[idx])
            idx += 1
        if max_range >= size - 1:
            return True
        else:
            return False
        