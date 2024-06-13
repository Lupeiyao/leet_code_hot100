from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            start, end = i + 1, len(nums) - 1
            while start < end:
                sum_val = nums[i] + nums[start] + nums[end]
                if sum_val < 0:
                    start += 1
                elif sum_val > 0:
                    end -= 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while end > start and nums[end] == nums[end + 1]:
                        end -= 1
        return result