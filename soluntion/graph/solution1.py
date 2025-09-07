from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result, row_size, col_size = 0, len(grid), len(grid[0])
        traveled = [[0] * col_size for i in range(row_size)]
        for i in range(row_size):
            for j in range(col_size):
                if traveled[i][j] == 1:
                    continue
                if grid[i][j] == '0':
                    traveled[i][j] = 1
                    continue
                result += 1
                queue = [(i, j)]
                traveled[i][j] = 1
                while queue:
                    cur_i, cur_j = queue.pop(0)
                    if 0 <= cur_i - 1 < row_size and grid[cur_i - 1][cur_j] == '1' and traveled[cur_i - 1][cur_j] == 0:
                        queue.append((cur_i - 1, cur_j))
                        traveled[cur_i - 1][cur_j] = 1
                    if 0 <= cur_i + 1 < row_size and grid[cur_i + 1][cur_j] == '1' and traveled[cur_i + 1][cur_j] == 0:
                        queue.append((cur_i + 1, cur_j))
                        traveled[cur_i + 1][cur_j] = 1
                    if 0 <= cur_j - 1 < col_size and grid[cur_i][cur_j - 1] == '1' and traveled[cur_i][cur_j - 1] == 0:
                        queue.append((cur_i, cur_j - 1))
                        traveled[cur_i][cur_j - 1] = 1
                    if 0 <= cur_j + 1 < col_size and grid[cur_i][cur_j + 1] == '1' and traveled[cur_i][cur_j + 1] == 0:
                        queue.append((cur_i, cur_j + 1))
                        traveled[cur_i][cur_j + 1] = 1
        return result


print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))