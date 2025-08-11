from typing import List

import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        row_start, row_end = 0, m - 1
        col_start, col_end = 0, n - 1
        for _ in range(math.ceil(min(m, n) / 2)):
            for j in range(col_start, col_end + 1):
                result.append(matrix[row_start][j])
            if row_start < row_end:
                for i in range(row_start + 1, row_end + 1):
                    result.append(matrix[i][col_end])
                for j in range(col_end - 1, col_start - 1, -1):
                    result.append(matrix[row_end][j])
                if row_start <= row_end - 1 and col_start < col_end:                
                    for i in range(row_end - 1, row_start, -1):
                        result.append(matrix[i][row_start])
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
        return result

print(Solution().spiralOrder([[2,5],[8,4],[0,-1]]))

