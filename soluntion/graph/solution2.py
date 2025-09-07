from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_size, col_size = len(grid), len(grid[0])
        queue = []
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 2:
                    queue.append((i, j))
        days = 0
        while queue:
            for _ in range(len(queue)):
                cur_i, cur_j = queue.pop(0)
                if 0 <= cur_i - 1 < row_size and grid[cur_i - 1][cur_j] == 1:
                    queue.append((cur_i - 1, cur_j))
                    grid[cur_i - 1][cur_j] = 2
                if 0 <= cur_i + 1 < row_size and grid[cur_i + 1][cur_j] == 1:
                    queue.append((cur_i + 1, cur_j))
                    grid[cur_i + 1][cur_j] = 2
                if 0 <= cur_j - 1 < col_size and grid[cur_i][cur_j - 1] == 1:
                    queue.append((cur_i, cur_j - 1))
                    grid[cur_i][cur_j - 1] = 2
                if 0 <= cur_j + 1 < col_size and grid[cur_i][cur_j + 1] == 1:
                    queue.append((cur_i, cur_j + 1))
                    grid[cur_i][cur_j + 1] = 2
            if queue:
                days += 1
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 1:
                    return -1
        return days
                
    

print(Solution().orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))
        
