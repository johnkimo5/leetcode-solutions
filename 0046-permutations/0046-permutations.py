class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # curr represents current list we are building
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        ans = []
        backtrack([])
        return ans
