import math

class Solution:
    def numSquares(self, n: int) -> int:
        result = [0, 1, 2, 3, 1]
        for num in range(5, n + 1):
            min_num = num
            for j in range(1, int(math.sqrt(num)) + 1):
                min_num = min(min_num, result[num - j * j] + 1)
            result.append(min_num)
        return result[n]
    
print(Solution().numSquares(9))
