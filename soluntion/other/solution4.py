from typing import List 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        size = len(nums)
        i = size - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i == -1:
            nums.reverse()
            return
        j = size - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp 
        swap(i, j)
        start, end = i + 1, size - 1
        while start < end:
            swap(start, end)
            start += 1
            end -= 1

x = [1,3,2]        
print(Solution().nextPermutation(x))
print(x)

        