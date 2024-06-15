from typing import List
import collections


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        # 递减栈帮助滑动最大值的时候，找到次大值
        stack = collections.deque()
        for i in range(k):
            push(stack, nums[i])
        result = [stack[0]]
        for i in range(1, len(nums) - k + 1):
            if nums[i - 1] == stack[0]:
                stack.popleft()
            result.append(max(stack[0], nums[i + k - 1]))
            push(stack, nums[i + k - 1])
        return result


def push(stack, val):
    while stack and val > stack[-1]:
        stack.pop()
    stack.append(val)

print(Solution2().maxSlidingWindow([1,-1], 1))