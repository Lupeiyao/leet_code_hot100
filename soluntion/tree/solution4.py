from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def help(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            return root1.val == root2.val and self.help(root1.left, root2.right) and self.help(root1.right, root2.left)
        

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        else:
            return self.help1(root.left, root.right)
        
    def help1(self, root1, root2):
        queue = [root1, root2]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                queue.extend([node1.left, node2.right, node1.right, node2.left])
        return True
        
            
left = TreeNode(2)
right = TreeNode(3)
root = TreeNode(1, left, right)
print(Solution().isSymmetric(root))