from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result, cur_queue = [], [root]
        while cur_queue:
            list_result = []
            for i in range(len(cur_queue)):
                node = cur_queue.pop(0)
                list_result.append(node.val)
                if node.left:
                    cur_queue.append(node.left)
                if node.right:
                    cur_queue.append(node.right)
            result.append(list_result)
        return result


        