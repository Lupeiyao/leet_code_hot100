from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)


        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        def buildTree(i, size):
            l = i * 2 + 1
            r = i * 2 + 2
            max_idx = i
            if l < size and nums[l] > nums[max_idx]:
                max_idx = l 
            if r < size and nums[r] > nums[max_idx]:
                max_idx = r
            if i != max_idx:
                swap(i, max_idx)
                buildTree(max_idx, size)

        for i in range(size // 2 - 1, -1 ,-1):
            buildTree(i, size)

        for i in range(1, k):
            swap(0, size - i)
            buildTree(0, size - i)
        return nums[0]
    
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
