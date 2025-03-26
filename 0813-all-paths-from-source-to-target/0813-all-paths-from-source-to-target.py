class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, currPath = [], [0]
        # iterate through every node
    
        # we can read the last variable and return that path
        # i represents the index we're going to on the graph
        def backtrack(currPath, i):
            if len(currPath) >= 1 and currPath[-1] == len(graph) - 1:
                ans.append(currPath.copy())
                return
            # have a for loop for the first index (which represents what 0 can go to )
            # this double adds
            for num in graph[i]:
                 # we should first add it
                currPath.append(num)
                backtrack(currPath, num)
                currPath.pop()
        backtrack(currPath, 0)
        return ans