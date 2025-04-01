from typing import List
from collections import Counter


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not self.is_valid(board):
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for s in "123456789":
                        board[i][j] = s
                        if self.solveSudoku(board):
                            return True
                        board[i][j] = '.'
                    return False

        return True


    def is_valid(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            col = [board[j][i] for j in range(9)]
            square = [
                board[x + (i // 3) * 3][y + (i % 3) * 3] 
                for x in range(3) 
                for y in range(3)
            ]

            if not self.check_list(row):
                return False
            if not self.check_list(col):
                return False
            if not self.check_list(square):
                return False


        return True

    def check_list(self, l: List[str]) -> bool:
        counts = Counter(l)
        for s in "123456789":
            if counts[s] > 1:
                return False
        return True

sol = Solution()

board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]

for row in board:
    print(row)

sol.solveSudoku(board)

for row in board:
    print(row)
