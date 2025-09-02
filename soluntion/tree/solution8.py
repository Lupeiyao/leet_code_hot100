from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur, stack = root, []
        pre_val = float('-inf')
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val < pre_val:
                return False
            else:
                pre_val = cur.val
            cur = cur.right 
        return True                