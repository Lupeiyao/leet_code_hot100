from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        size = len(nums)
        max_range = nums[0]
        idx = 1
        while idx <= max_range and idx < size:
            result += 1
            if max_range >= size - 1:
                return result
            for i in range(idx, max_range + 1):
                max_range = max(max_range, i + nums[i])
                idx += 1
        return result
    
print(Solution().jump([2,3,0,1,4]))