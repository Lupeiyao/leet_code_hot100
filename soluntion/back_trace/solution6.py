from typing import List
from collections import Counter

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = len(board[0])
        traveled = [[0] * col_size for _ in range(row_size)]

        cnt = Counter(c for row in board for c in row)
        if not cnt>=Counter(word):
            return False

        def help(word: str, row : int, col : int):
            if "" == word:
                return True
            if row < 0 or row >= row_size:
                return False
            if col < 0 or col >= col_size:
                return False
            if traveled[row][col] == 1:
                return False
            if word[0] == board[row][col]:
                traveled[row][col] = 1
                tag = help(word[1:], row - 1, col) or help(word[1:], row + 1, col) or help(word[1:], row, col - 1) or help(word[1:], row, col + 1)
                traveled[row][col] = 0
                return tag
            else:
                return False
        
        for i in range(row_size):
            for j in range(col_size):
                if help(word, i, j):
                    return True
        return False
