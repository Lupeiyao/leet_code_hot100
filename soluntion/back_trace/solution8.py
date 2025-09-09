from typing import List

class Solution:


    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        queen_cols = set()
        result = []
        
        def help(queen_size: int, i: int):
            for j in range(n):
                flat = False
                for queen in queens:
                    if j == queen[1] or abs(i - queen[0]) == abs(j - queen[1]):
                        flat = True
                        break
                if flat:
                    continue
                queens.append((i, j))
                queen_cols.add(j)
                tmp = [['.'] * n for _ in range(n)]
                if queen_size == 1:
                    for queen in queens:
                        tmp[queen[0]][queen[1]] = 'Q'
                    result.append(["".join(x) for x in tmp])
                else:
                    help(queen_size - 1, i + 1)
                queens.pop()
                queen_cols.remove(j)
        help(n, 0)
        return result


print(Solution().solveNQueens(1))