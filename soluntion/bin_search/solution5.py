from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        left, right = 0, size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

print(Solution().findMin([4,5,6,1,2,3]))
