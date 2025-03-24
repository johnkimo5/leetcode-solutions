class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(curr, i):
            # decision tree is to either include the element or not
            if i == len(nums):
                ans.append(curr.copy())
                return
            # include element
            curr.append(nums[i])
            backtracking(curr, i + 1)
            curr.pop()
            backtracking(curr, i + 1)
        backtracking([], 0)
        return ans