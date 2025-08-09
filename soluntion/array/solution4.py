from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        length = len(nums)
        pre_left, pre_right = 1, 1
        for i in range(1, length):
            pre_left *= nums[i - 1]
            pre_right *= nums[-i]
            result[i] *= pre_left
            result[-i - 1] *= pre_right
        return result

    
print(Solution().productExceptSelf([1,2,3,4]))