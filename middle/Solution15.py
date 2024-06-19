from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix[0]) - 1
        for j in range(len(matrix[0])):
            if target <= matrix[0][j]:
                right = j
                break

        down = len(matrix) - 1
        for i in range(len(matrix)):
            if target <= matrix[i][0]:
                down = i
                break

        for i in range(down + 1):
            for j in range(right + 1):
                if matrix[i][j] == target:
                    return True
        return False


print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
