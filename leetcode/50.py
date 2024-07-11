from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = ["." for i in range (0, n)]
        solutions = []
        self.solve(n, [list(row) for i in range(0, n)], solutions)
        solutions.sort()
        return solutions

    def solve(self, n: int, board: List[List[str]], solutions: List[List[str]]):
        if n == 0:
            ans = ["".join(row) for row in board]
            solutions.append(ans)
            return

        queen_positions = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "Q":
                    queen_positions.append((i, j))
        queen_positions.sort()

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != "Q" and self.is_valid(queen_positions, i, j):
                    board[i][j] = "Q"
                    self.solve(n - 1, board, solutions)
                    board[i][j] = "."

        return []

    def is_valid(self, queen_positions, row, col) -> bool:
        for i, j in queen_positions:
            if i == row or j == col or abs(i - row) == abs(j - col):
                return False

        return True

sol = Solution()
print(sol.solveNQueens(7))
# print(sol.solveNQueens(1))
