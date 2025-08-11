from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start, end = 0, len(matrix) - 1
        for _ in range(len(matrix) // 2):
            for i in range(end - start):
                tmp = matrix[start][start + i]
                matrix[start][start + i] = matrix[end - i][start]
                matrix[end - i][start] = matrix[end][end - i]
                matrix[end][end - i] = matrix[start + i][end]
                matrix[start + i][end] = tmp
            start += 1
            end -= 1
        return matrix
    

print(Solution().rotate([
    [2,29,20,26,16,28],
    [12,27,9,25,13,21],
    [32,33,32,2,28,14],
    [13,14,32,27,22,26],
    [33,1,20,7,21,7],
    [4,24,1,6,32,34]]))


