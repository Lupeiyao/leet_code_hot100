from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cur_idx = 0
        for num in nums:
            if num != 0:
                nums[cur_idx] = num
                cur_idx += 1
        for idx in range(cur_idx, len(nums)):
            nums[idx] = 0
            