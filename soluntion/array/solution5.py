from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while 1 <= nums[i] <= length and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
                
        for i in range(length):
            if i != nums[i] - 1:
                return i + 1
        return length + 1
    

print(Solution().firstMissingPositive([3,4,-1,1]))