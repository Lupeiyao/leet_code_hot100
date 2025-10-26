

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        result = 0
        pre2, pre1 = 1, 2
        for _ in range(3, n + 1):
            result = pre2 + pre1
            pre2 = pre1
            pre1 = result
        return result
    