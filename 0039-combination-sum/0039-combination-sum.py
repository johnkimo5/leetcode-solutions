"""
keep going down until your sum is greater than target, once it's greater than return and backtrack 
if it's equal to target, append to answer list and return

"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def backtrack(curr, currSum, i):
            if currSum > target or i >= len(candidates):
                # we need to backtrack
                return
            if currSum == target:
                ans.append(curr[:])
                return
            curr.append(candidates[i])
            backtrack(curr, currSum + candidates[i], i)
            curr.pop()
            backtrack(curr, currSum, i + 1)
        backtrack([], 0, 0)
        return ans
