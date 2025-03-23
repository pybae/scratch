from typing import List

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True

        return False

    def dfs(self, board: List[List[str]], word: str, i: int, j: int) -> bool:
        if not word:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if word[0] != board[i][j]:
            return False

        board[i][j] = ""
        result = (self.dfs(board, word[1:], i - 1, j) or
                  self.dfs(board, word[1:], i + 1, j) or
                  self.dfs(board, word[1:], i, j - 1) or
                  self.dfs(board, word[1:], i, j + 1))
        board[i][j] = word[0]

        return result


sol = Solution()
# print(sol.exist(
#     [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
#     "ABCCED"
# ))

print(sol.exist(
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    "ABCB"
))
