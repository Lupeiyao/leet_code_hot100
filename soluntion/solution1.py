from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) < 2:
            return []
        num_to_index = {}
        for (idx, num) in enumerate(nums):
            if target - num in num_to_index:
                return [idx, num_to_index[target - num]]
            else:
                num_to_index[num] = idx
        return []


Solution().twoSum([3,3,3], 10)

    