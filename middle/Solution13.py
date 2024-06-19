from typing import List

class Solution13:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result, cnt = [], min((len(matrix) + 1) // 2, (len(matrix[0]) + 1) // 2)
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        for start in range(cnt):
            for j in range(left, right + 1):
                result.append(matrix[up][j])
            for i in range(up + 1, down + 1):
                result.append(matrix[i][right])
            if up != down:
                for j in range(right - 1, left - 1, -1):
                    result.append(matrix[down][j])
            if left != right:
                for i in range(down - 1, up, -1):
                    result.append(matrix[i][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return result

print(Solution13().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))



