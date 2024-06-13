from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2idx = dict()
        for i in range(len(nums)):
            if target - nums[i] in num2idx:
                return [i, num2idx[target - nums[i]]]
            else:
                num2idx[nums[i]] = i
