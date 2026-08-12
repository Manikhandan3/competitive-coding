class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[i][j] !=  ".":
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] !=  ".":
                    if board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])
        
        for k in range(len(board)):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (k // 3) * 3 + i
                    c = (k % 3) * 3 + j
                    if board[r][c] !=  ".":
                        if board[r][c] in seen:
                            return False
                        else:
                            seen.add(board[r][c])
        
        return True
        
