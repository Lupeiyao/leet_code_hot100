from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.help(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
    
    def findNodeIdx(self, inorder: List[int], in_start: int, in_end: int, val: int):
        for i in range(in_start, in_end + 1):
            if inorder[i] == val:
                return i


    def help(self, preorder: List[int], pre_start: int, pre_end: int, inorder: List[int], in_start: int, in_end: int) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None
        root = TreeNode(preorder[pre_start])
        if pre_start == pre_end:
            return root
        if pre_start < pre_end:
            mid_idx = self.findNodeIdx(inorder, in_start, in_end, preorder[pre_start])
            left_length = mid_idx - in_start
            left_node = self.help(preorder, pre_start + 1, pre_start + left_length, inorder, in_start, mid_idx - 1)
            right_node = self.help(preorder, pre_start + left_length + 1, pre_end, inorder, mid_idx + 1, in_end)
            root.left = left_node
            root.right = right_node
        return root



Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])