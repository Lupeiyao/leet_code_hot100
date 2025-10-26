from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        dp_max = [0] * size
        dp_min = [0] * size 
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1, size):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        return max(dp_max)

            
    

print(Solution().maxProduct([2,3,-2,4]))

