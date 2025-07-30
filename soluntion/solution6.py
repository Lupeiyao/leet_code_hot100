from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for (idx, num) in enumerate(nums):
            if num > 0:
                break
            if idx > 0 and nums[idx - 1] == num:
                continue
            start, end = idx + 1, len(nums) - 1
            while start < end:
                sum_val = num + nums[start] + nums[end]
                if sum_val < 0:
                    start += 1
                elif sum_val > 0:
                    end -= 1
                else:
                    result.append([num, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

        return result

            
print(Solution().threeSum([1, -1, -1, 0]))