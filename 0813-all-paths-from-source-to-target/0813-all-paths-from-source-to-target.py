class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, currList = [], [0]
        def backtrack(currList, i):
            if i == len(graph) - 1:
                ans.append(currList.copy())
                return
            nums = graph[i]
            for num in nums:
                currList.append(num)
                backtrack(currList, num)
                currList.pop()
        backtrack(currList, 0)
        return ans
