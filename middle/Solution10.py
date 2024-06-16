from typing import List


class Solution10:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k == 0:
            return
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


def reverse(nums, start, end):
    while start < end:
        temp = nums[end]
        nums[end] = nums[start]
        nums[start] = temp
        start += 1
        end -= 1
