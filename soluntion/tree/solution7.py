from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def help(self, nums: List[int], start, end):
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        if start < end:
            if start < end - 1:
                root.left = self.help(start, mid - 1)
            root.right = self.help(mid + 1, end)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.help(nums, 0, len(nums) - 1)
