from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_val = sum(nums)
        size = len(nums)
        if sum_val % 2 == 1:
            return False
        target = sum_val // 2
        dp = [[0] * (target + 1) for _ in range(size)]
        dp[0][0] =  1
        if(nums[0] <= target):
            dp[0][nums[0]] = 1
        for i in range(1, size):
            dp[i][0] = 1
            for j in range(target + 1):
                if dp[i - 1][j] == 1:
                    dp[i][j] = 1
                elif j >= nums[i] and dp[i - 1][j - nums[i]] == 1:
                    dp[i][j] = 1
            if dp[i][target] == 1:
                return True
        return False
    
print(Solution().canPartition([100,4,6]))
            