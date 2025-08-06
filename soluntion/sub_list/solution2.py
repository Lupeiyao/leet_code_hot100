from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        result, stack = [], []
        for i in range(k):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                stack.pop(-1)
            stack.append(i)
        result.append(nums[stack[0]])

        for i in range(k, len(nums)):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                stack.pop(-1)
            stack.append(i)
            if stack[0] <= i - k:
                stack.pop(0)
            result.append(nums[stack[0]])
        return result
        