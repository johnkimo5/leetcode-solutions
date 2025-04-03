class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # graph[i] is a list of all nodes you can visit from node i
        n = len(graph)
        # i represents the index that we are looking at 
        def backtrack(i, currPath):
            # what's the constraint
            if currPath[-1] == n - 1:
                ans.append(currPath.copy())
                return
            nums = graph[i]
            for num in nums:
                currPath.append(num)
                backtrack(num, currPath)
                currPath.pop()
            
        ans = []
        backtrack(0, [0])
        return ans

