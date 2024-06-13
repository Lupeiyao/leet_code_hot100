from typing import List


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        if nums is None or len(nums) < 2:
            return
        start = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                start = i
                break
        if start == -1:
            return
        for i in range(start + 1, len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
                nums[i] = 0



