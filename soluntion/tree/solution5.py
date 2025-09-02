from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def __init__(self):
        self.result = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        if root:
            left_max = self.maxDepth(root.left)
            right_max = self.maxDepth(root.right)
            result = 1 + max(left_max, right_max)
            self.result = max(self.result, left_max + right_max)
        return result
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.result
        