from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        length = len(nums)
        if k != 0:
            self.reverse(nums, 0, length - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, length - 1)
        


    def reverse(self, nums, start, end):
        while start < end:
            tmp = nums[end]
            nums[end] = nums[start]
            nums[start] = tmp
            start += 1
            end -= 1

    
print(Solution().rotate([1,2,3,4,5,6,7], 3))


            