class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r - c
        negDiag = set() # r + c
        board = [["."] * n for i in range(n)]
        ans = []
        def backtrack(r): # i parameter is the row #
            # base case
            if r == n:
                # copy board to our solution
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            # go through every column
            for c in range(n):
                if c in col or r - c in posDiag or r + c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r - c)
                negDiag.add(r + c)
                board[r][c] = "Q"
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r - c)
                negDiag.remove(r + c)
                board[r][c] = "."
        backtrack(0)
        return ans
            # add to board
            # backtrack to next row
            # pop from board
