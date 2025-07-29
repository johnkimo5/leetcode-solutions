from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        n = len(image)
        m = len(image[0])

        originalColor = image[sr][sc]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        queue = deque([(sr, sc)])

        def isValid(x, y):
            if 0 <= x < n and 0 <= y < m and image[x][y] == originalColor:
                return True
            return False

        visited = set((sr, sc))
        while queue:
            x, y = queue.popleft()
            image[x][y] = color
            for dx, dy in directions:
                if isValid(dx + x, dy + y):
                    visited.add((dx + x, dy + y))
                    queue.append((dx + x, dy + y))

        return image
