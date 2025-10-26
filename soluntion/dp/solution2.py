
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(numRows):
            sub_result = []
            result.append(sub_result)
            for col in range(row + 1):
                if col == 0 or col == row:
                    sub_result.append(1)
                else:
                    sub_result.append(result[row - 1][col - 1] + result[row - 1][col])
        return result

print(Solution().generate(3))