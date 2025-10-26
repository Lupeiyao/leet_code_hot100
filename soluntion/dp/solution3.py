from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = [0]
        dp1 = [nums[0]]
        for i in range(1, len(nums)):
            dp0.append(max(dp0[i - 1], dp1[i - 1]))
            dp1.append(nums[i] + dp0[i - 1])
        return max(dp0[-1], dp1[-1])
    