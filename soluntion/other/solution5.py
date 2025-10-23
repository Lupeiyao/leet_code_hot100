from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        size = len(nums)
        i = size - 1
        while nums[nums[0]] != nums[0]:
            swap(0, nums[0])
        return nums[0]
    
print(Solution().findDuplicate([1,2,2,3,4,5]))