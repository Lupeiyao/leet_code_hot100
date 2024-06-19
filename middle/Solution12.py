from typing import List


class Solution12:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = [1] * len(matrix)
        col = [1] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0
        print(matrix)


Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])