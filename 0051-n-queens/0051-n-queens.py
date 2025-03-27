class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # how to implement the bounds? 
        ans = []
        colSet = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        board = [["."] * n for i in range(n)]
        print(board)
        # where index represents row and val represents col
        def backtrack(r):
            if r == n:
                # copy this answer
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            for c in range(n):
                if c in colSet or r + c in posDiag or r - c in negDiag:
                    continue
                # add it
                colSet.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                # backtrack
                backtrack(r + 1)

                colSet.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return ans
                
            

