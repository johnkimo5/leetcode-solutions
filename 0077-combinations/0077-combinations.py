"""
all possible combinations -> [1, 2] and [2, 1] are the same
we need to generate combinations,
we need to actual build the list -> perform backtracking

"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(curr, num):
            if len(curr) == k:
                ans.append(curr[:])
                return
            # if there's way to fix this, it's chanigng the bottom range 
            for i in range(num, n + 1):
                if i not in curr:
                    curr.append(i)
                    backtracking(curr, i + 1)
                    curr.pop()
        ans = []
        backtracking([], 1)
        return ans
