from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        if root:
            result = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return result