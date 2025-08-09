from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(nums[i] + max(dp[i -1], 0))
            result = max(result, dp[i])
        return result
    

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))