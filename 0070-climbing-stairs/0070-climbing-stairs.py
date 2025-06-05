class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(steps, cache):
            if steps > n:
                return 0
            if steps == n:
                return 1
            if steps in cache:
                return cache[steps]
            cache[steps] = dfs(steps + 1, cache) + dfs(steps + 2, cache)
            return cache[steps]
        return dfs(0, {})