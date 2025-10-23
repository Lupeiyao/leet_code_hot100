from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result
    

print(Solution().singleNumber([1,1,2,2,3,3,10,10,11]))
