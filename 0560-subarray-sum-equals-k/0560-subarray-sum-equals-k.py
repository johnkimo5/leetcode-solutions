"""
intuition: the difference between two prefix sums is equal to a subarray's sum
if this subarray's sum equals k, increment answer
hashmap
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # find the prefix sums
        prefixSum = {0 : 1} # map sum to # of subarrays with this
        currSum = 0
        ans = 0
        for i in range(len(nums)):
            currSum += nums[i]     
            if currSum - k in prefixSum:
                ans += prefixSum[currSum - k]
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        return ans
        # iterate over the prefix sum
    