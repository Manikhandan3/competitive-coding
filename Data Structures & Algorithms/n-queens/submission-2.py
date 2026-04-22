class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []

        def dfs(i):
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for k in range(n):
                if self.safe(i,k,board):
                    board[i][k] = 'Q'
                    dfs(i+1)
                    board[i][k] = '.'
        dfs(0)
        return res

    def safe(self,r,c,board):
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1
            while row >= 0 and col < len(board):
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True

