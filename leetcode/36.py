from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            if not self.checkRow(board, i):
                return False

            if not self.checkCol(board, i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.checkGrid(board, i, j):
                    return False

        return True

    def checkRow(self, board, row_number) -> bool:
        numbers = set([str(i) for i in range(0, 10)])
        for number in board[row_number]:
            if number != ".":
                if number not in numbers:
                    return False
                numbers.remove(number)

        return True

    def checkCol(self, board, col_number) -> bool:
        numbers = set([str(i) for i in range(0, 10)])
        for i in range(0, 9):
            number = board[i][col_number]
            if number != ".":
                if number not in numbers:
                    return False
                numbers.remove(number)

        return True

    def checkGrid(self, board, row_number, col_number) -> bool:
        numbers = set([str(i) for i in range(0, 10)])
        for i in range(0, 3):
            for j in range(0, 3):
                number = board[row_number + i][col_number + j]
                if number != ".":
                    if number not in numbers:
                        return False
                    numbers.remove(number)

        return True


sol = Solution()
board = [["9","3",".",".","7",".",".",".","."]
		 ,["6",".",".","1","9","5",".",".","."]
		 ,[".","9","8",".",".",".",".","6","."]
		 ,["8",".",".",".","6",".",".",".","3"]
		 ,["4",".",".","8",".","3",".",".","1"]
		 ,["7",".",".",".","2",".",".",".","6"]
		 ,[".","6",".",".",".",".","2","8","."]
		 ,[".",".",".","4","1","9",".",".","5"]
		 ,[".",".",".",".","8",".",".","7","9"]]

print(sol.isValidSudoku(board))
