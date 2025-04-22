class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set() # set of tuples
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # make sure it's not in a set we've already visited
            # we'll only call dfs when it is in bounds so don't worry about this
            # it'd be better if we try returning the max
            visited.add((r,c))
            area = 1 # add it for the specific branch 
            for dr, dc in directions:
                nR = r + dr
                nC = c + dc
                if 0 <= nR < rows and 0 <= nC < cols and grid[nR][nC] == 1 and (nR, nC) not in visited:
                    area += dfs(nR, nC)
            return area

        area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = max(area, dfs(row, col))
        return area