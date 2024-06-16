from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_size = len(nums)
        for i in range(num_size):
            while 0 <= nums[i] - 1 < num_size and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

        for i in range(num_size):
            if nums[i] - 1 != i:
                return i + 1
        return num_size + 1


print(Solution().firstMissingPositive([1,2,0]))