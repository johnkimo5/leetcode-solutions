class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # may contain duplicates, return all possible subsets, sort it
        nums.sort()
        outputList, currList = [], []
        def helper(i, outputList, currList):
            if i == len(nums):
                outputList.append(currList.copy())
                return
            currList.append(nums[i])
            helper(i + 1, outputList, currList)
            currList.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, outputList, currList)
        helper(0, outputList, currList)
        return outputList
            
