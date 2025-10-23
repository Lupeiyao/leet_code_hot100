from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        zero_idx, cur, two_idx = -1, 0, len(nums)
        while cur < two_idx:
            if nums[cur] == 0:
                swap(zero_idx + 1, cur)
                zero_idx += 1
                cur += 1
            elif nums[cur] == 2:
                swap(two_idx - 1, cur)
                two_idx -= 1
            else:
                cur += 1


            
        