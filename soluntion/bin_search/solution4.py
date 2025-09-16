from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left, right = 0, size - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            




print(Solution().search([100,0,1], 100))        
