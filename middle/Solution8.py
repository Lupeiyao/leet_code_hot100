from typing import List


class Solution8:
    def maxSubArray(self, nums: List[int]) -> int:
        # min_val记录所有之前子数组和中的最小值
        min_val, result, sum_val = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            sum_val += nums[i]
            if min_val < 0:
                result = max(result, sum_val - min_val)
            else:
                result = max(result, sum_val)
            min_val = min(min_val, sum_val)
        return result


print(Solution().maxSubArray( [-2,1,-3,4,-1,2,1,-5,4]))