from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if not root:
            return 0

        def rootSum(root, targetSum):
            if not root:
                return 0
            result = 0
            if root.val == targetSum:
                result += 1
            result += rootSum(root.left, targetSum - root.val)
            result += rootSum(root.right, targetSum - root.val)
            return result
        
        result = rootSum(root, targetSum)
        result += self.pathSum(root.left, targetSum)
        result += self.pathSum(root.right, targetSum)
        return result
    
    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return
            result = 0
            curr += root.val
            prefix[curr] += 1
            result += prefix[curr - targetSum]
            result += dfs(root.left, curr)
            result += dfs(root.right, curr)
            prefix[curr] -= 1
            return result

        return dfs(root, 0)

            
            
