from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root:
            if not root.left and not root.right:
                return
            if not root.left:
                self.flatten(root.right)
            elif not root.right:
                self.flatten(root.left)
                root.right = root.left
                root.left = None
            else:
                self.flatten(root.left)
                self.flatten(root.right)
                right = root.right
                root.right = root.left
                root.left = None
                while root.right:
                    root = root.right
                root.right = right


root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
Solution().flatten(root)
pass